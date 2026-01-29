from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CourierIncident(models.Model):
  _name = "courier.incident"
  _description = "Courier Incident"
  _order = "incident_datetime desc"
  
  name = fields.Char(required=True)

  customer_id = fields.Many2one(
    "res.partner",
    string="Customer",
    required=True,
)

  shipment_id = fields.Many2one(
      "res.partner",
      string="Shipment / Resi",
      required=True,
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

  _sql_constraints = [
    (
      "incident_unique",
      "unique(customer_id, incident_type, incident_datetime)",
      "Incident already exists for this customer and time.",
    )
  ]

  def action_mark_followup(self):
    self.write({"state": "followup"})
    
  def action_resolve(self):
    self.write({
        "state": "done",
        "resolved_at": fields.Datetime.now(),
    })
    
  @api.constrains("state", "followup_note")
  def _check_followup_note(self):
    for rec in self:
      if rec.state == "done" and not rec.followup_note:
        raise ValidationError(
          "Follow-up note is required before resolving the incident."
        )