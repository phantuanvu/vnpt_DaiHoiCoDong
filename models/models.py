from openerp import models, fields, api

class bieu_quyet(models.Model):
    _name = 'bieu_quyet.bieu_quyet'

    day = fields.Date(string='Ngay uy Quyen')
    name = fields.Char(string ='Nguoi Uy Quyen')
    last_name = fields.Char(string='Nguoi Nhan Uy Quyen')
    co_phan = fields.Char(string='So Co Phan Uy Quyen')
    hinh_thuc = fields.Selection([('m','Mail'),('SDT','So Dien Thoai'),('GUQ','Giay Uy Quyen')],string='Hinh thuc')
    chi_tiet = fields.Char(string='Chi Tiet Gui Cho Ai')
    gender = fields.Selection([('m','Male'),('f','Female')],string='Gender')
    is_active =fields.Boolean(string="Active")
    birth_date =fields.Date(string='Birth Date')
