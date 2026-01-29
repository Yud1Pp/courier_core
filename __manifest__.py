{
  "name": "Courier Incident Log",
  "version": "1.0.0",
  "depends": ["base"],
  "author": "Yudi Pratama Putra",
  "category": "Operations",
  "description": """
    Internal incident logging module for courier operations.
    Allows teams to record, follow up, and resolve operational incidents.
  """,
  "data": [
    "security/ir.model.access.csv",
    "views/courier_incident_views.xml",
  ],
  "installable": True,
  "application": False,
}