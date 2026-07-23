import json
from schemas import LEAD_SCHEMA, INVOICE_SCHEMA, TICKET_SCHEMA

print("Lead Schema")
print(json.dumps(LEAD_SCHEMA, indent=4))

print("\nInvoice Schema")
print(json.dumps(INVOICE_SCHEMA, indent=4))

print("\nSupport Ticket Schema")
print(json.dumps(TICKET_SCHEMA, indent=4))