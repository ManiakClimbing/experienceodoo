from odoo import api,models,fields
class classcitadel (models.Model):
    _name ='classname'
    level = fields.Selection([('basic', 'basic'),('intermediate','intermediate'),('advanced','advanced')])
    SessionAvailable = fields.One2many('session.name','classofthesession')
    
    
class sessioncitadel(models.Model):
    _name ='session.name'
    startSession = fields.Datetime()
    endSession = fields.Datetime()
    classofthesession = fields.Many2one('classname')
    maester = fields.Many2one('res.partner')
    students = fields.Many2many('res.partner')
    
    
