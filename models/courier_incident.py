from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CourierIncident(models.Model):
  _name = "courier.incident"
  _description = "Courier Incident"
  _order = "incident_datetime desc"
  
  name = fields.Char(required=True)

  customer_id = fields.Many2one(
    "courier.customer",
    string="Customer",
    required=True,
  )
  
  shipment_id = fields.Many2one(
    "courier.shipment",
    string="Shipment",
  )
  
  incident_type = fields.Selection(
    [
      ("health", "Health"),
      ("lost_item", "Lost Item"),
      ("delay", "Delay"),
      ("other", "Other"),
    ],
    default="other",
  )
  
  incident_datetime = fields.Datetime(
    required=True,
    default=fields.Datetime.now,
  )
  
  severity = fields.Selection(
    [
      ("low", "Low"),
      ("medium", "Medium"),
      ("high", "High"),
    ],
    default="low",
  )

  description = fields.Text()

  followup_note = fields.Text()

  state = fields.Selection(
    [
      ("draft", "Draft"),
      ("followup", "Follow-up"),
      ("done", "Done"),
    ],
    default="draft",
  )
  
  resolved_at = fields.Datetime(readonly=True)
