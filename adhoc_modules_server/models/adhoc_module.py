# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api
# from openerp.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)


class AdhocModuleModule(models.Model):
    _inherit = 'ir.module.module'
    _name = 'adhoc.module.module'

    repository_id = fields.Many2one(
        'adhoc.module.repository',
        'Repository',
        ondelete='cascade',
        required=True,
        auto_join=True,
        )
    dependencies_id = fields.One2many(
        'adhoc.module.dependency',
        'module_id',
        'Dependencies',
        readonly=True,
        )

    @api.model
    def create(self, vals):
        # ir module modifies create, we need default one
        create_original = models.BaseModel.create
        module = create_original(self, vals)
        module_metadata = {
            'name': 'module_%s_%s' % (
                vals['name'],
                module.repository_id.branch.replace('.', '_')),
            'model': self._name,
            'module': 'adhoc_module',
            'res_id': module.id,
            'noupdate': True,
        }
        self.env['ir.model.data'].create(module_metadata)
        return module

    @api.multi
    def _update_dependencies(self, depends=None):
        self.ensure_one()
        if depends is None:
            depends = []
        existing = set(x.name for x in self.dependencies_id)
        needed = set(depends)
        for dep in (needed - existing):
            self._cr.execute(
                'INSERT INTO adhoc_module_dependency (module_id, name) '
                'values (%s, %s)', (self.id, dep))
        for dep in (existing - needed):
            self._cr.execute(
                'DELETE FROM adhoc_module_dependency WHERE module_id = %s '
                'and name = %s', (self.id, dep))
        self.invalidate_cache(['dependencies_id'])
