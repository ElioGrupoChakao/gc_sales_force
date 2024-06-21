# models/models.py
# from odoo import models, api

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     @api.model
#     def search(self, args, **kwargs):
#         user = self.env.user
#         if user.has_group('gc_sales_force.group_sales_force_user'):
#             args = args + [('user_id', '=', user.id)]
#         return super(SaleOrder, self).search(args, **kwargs)

# class AccountMove(models.Model):
#     _inherit = 'account.move'

#     @api.model
#     def search(self, args, **kwargs):
#         user = self.env.user
#         if user.has_group('gc_sales_force.group_sales_force_user'):
#             args = args + [('user_id', '=', user.id)]
#         return super(AccountMove, self).search(args, **kwargs)

# class AccountPayment(models.Model):
#     _inherit = 'account.payment'

#     @api.model
#     def search(self, args, **kwargs):
#         user = self.env.user
#         if user.has_group('gc_sales_force.group_sales_force_user'):
#             args = args + [('user_id', '=', user.id)]
#         return super(AccountPayment, self).search(args, **kwargs)
