# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class booking_addon(models.Model):
    _name="booking.addon"
    
    name=fields.Char('Addon Name')