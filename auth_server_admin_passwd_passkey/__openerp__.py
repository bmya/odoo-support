# -*- encoding: utf-8 -*-
{
    'name': 'Authentification - Admin Passkey',
    'version': '8.0.2.1.2',
    'category': 'base',
    'description': """
Server Admin password become a passkey for all active logins
============================================================

Functionality :
---------------
* You can now login with any user using server admin password
(admin_passwd parameter) or with admin user password (superuser password)
    """,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'base',
        # arreglar error de mandar email por misma clave
        'auth_admin_passkey',
    ],
    'data': [
    ],
    'demo': [],
    'js': [],
    'css': [],
    'qweb': [],
    'images': [],
    'post_load': '',
    'installable': True,
    'auto_install': False,
}
