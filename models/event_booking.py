# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

e_type=[
('Associations', 'associations'),
('Award Ceremony', 'award_ceremony'),
('Banquet', 'banquet'),
('Brand Sale', 'brand_sale'),
('City Promotion', 'city_promotion'),
('Comedy Show', 'comedy_show'),
('Concert', 'concert'),
('Conference', 'conference'),
('Convention', 'convention'),
('Exhibition', 'exhibition'),
('Fashion Show', 'fashion_show'),
('Graduation', 'graduation'),
('Live Event', 'live_event'),
('Other', 'other'),
('Product Launch', 'product_launch'),
('Special Events', 'special_events'),
('Sports', 'sports'),
('Theatre', 'theatre'),
('Training Institute', 'training_institute'),
('Wedding', 'wedding'),
('Workshop', 'workshop'),
    
    ]

class event_booking(models.Model):
    _name="event.booking"
    _inherits={'res.partner':'partner_id'}
    
    event_type=fields.Selection(e_type,string="Event type")
    date_from = fields.Date('From')
    date_to= fields.Date('To')
    attending_number = fields.Integer('Number of Attendees')
    addon_ids=fields.Many2many('booking.addon','Addons')
    comments=fields.Text('Comments')
    partner_id = fields.Many2one('res.partner',string="Partner")
    org_name=fields.Char('Organisation Name')