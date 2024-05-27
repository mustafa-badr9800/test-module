from odoo import http
import json


class ProductApi(http.Controller):
    @http.route('/get_product_data', type="json", auth="none", methods=["GET"], csrf=False)
    def get_product_data(self):
        request_data = json.loads(http.request.httprequest.data)
        if request_data:
            product_name = request_data.get("name")
            product = http.request.env['product.template'].sudo().search([('name', '=', product_name)], limit=1)
            if product:
                return {
                    'status': 200,
                    'message': 'success',
                    'data': {
                        'product_id': product.id,
                        'product_name': product.name,
                        'product_api_field': product.api_field,
                    }
                }
            else:
                return {
                    'status': 400,
                    'message': 'No Product Found',
                }

        else:
            return {
                'status': 400,
                'message': 'No Body Provided',
            }
