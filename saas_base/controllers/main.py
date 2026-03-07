# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import odoo.service.db
import logging

_logger = logging.getLogger(__name__)


class SaasBaseController(http.Controller):

    @http.route('/saas/create_db', type='http', auth='public', website=True)
    def create_db_form(self, **kwargs):
        return request.render('saas_base.create_db_form', {})

    @http.route('/saas/create_db/submit', type='http', auth='public', methods=['POST'], website=True, csrf=False)
    def create_db_submit(self, **kwargs):
        db_name = kwargs.get('db_name')
        admin_password = kwargs.get('admin_password')
        lang = 'es_PE' 

        if not db_name or not admin_password:
            return request.render('saas_base.create_db_form', {'error': 'Todos los campos son obligatorios'})

        # Validar que no exista la base de datos
        if db_name in odoo.service.db.list_dbs():
            return request.render('saas_base.create_db_form', {'error': 'La base de datos ya existe'})

        try:
            # La creación de la base de datos incluye la creación del filestore automáticamente por Odoo
            # exp_create_database(db_name, demo, lang, password)
            odoo.service.db.exp_create_database(db_name, False, lang, admin_password)
            
            return request.render('saas_base.create_db_success', {'db_name': db_name, 'message': 'Base de datos creada exitosamente'})
        except Exception as e:
            _logger.exception("Error al crear la base de datos")
            return request.render('saas_base.create_db_form', {'error': f'Error al crear la base de datos: {str(e)}'})
