# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import UserError


class SingleInvoiceWizard(models.TransientModel):
    _name = "sh.single.invoice.wizard"
    _description = "Single Invoice Wizard"

    confirmation_message = fields.Text(string="", readonly=True, )
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    sale_order_ids = fields.Many2many('sale.order', string="Sale Orders")

    def confirm_create_single_invoice(self):

        self.sale_order_ids._create_invoices()

        if self._context.get('open_invoices', False):
            return self.sale_order_ids.action_view_invoice()

        return {'type': 'ir.actions.act_window_close'}

    def create_single_invoice(self):

        active_ids = self.env.context.get('active_ids')
        active_model = self.env.context.get('active_model')
        active_id = self.env.context.get('active_id')

        if len(active_ids) > 0:
            active_ids.sort()
            sale_order_model = self.env[active_model].browse(active_id)

            for each_id in active_ids:
                each_sale_order_model = self.env[active_model].browse(
                    each_id)
                if each_sale_order_model.partner_id.id != sale_order_model.partner_id.id:
                    raise UserError("Partners Must be Same !")
                if each_sale_order_model.state != 'sale':
                    raise UserError(
                        "Only Confirm sale order are consider for create invoice !")
                if each_sale_order_model.invoice_count != 0:
                    raise UserError(
                        "Invoice Already created for this sale order !")

                invoiceable_lines = each_sale_order_model._get_invoiceable_lines()

                if len(invoiceable_lines.ids) != len(each_sale_order_model.order_line.ids):
                    raise UserError(
                        _('There is no invoiceable line. If a product has a Delivered quantities invoicing policy, please make sure that a quantity has been delivered.'))

        return {
            'name': 'Create Single Invoice',
            'res_model': 'sh.single.invoice.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('sh_create_single_invoice.view_single_invoice_wizard').id,
            'context': {
                'default_confirmation_message': "Do you want to create single invoice?",
                'default_sale_order_id': active_id,
                'default_sale_order_ids': [(6, 0, active_ids)],

            },
            'target': 'new',
            'type': 'ir.actions.act_window'
        }
