from examples import EXAMPLES

def classify_ticket(ticket):
    ticket = ticket.lower()

    if any(word in ticket for word in ["refund", "payment", "charged", "invoice"]):
        return "Billing"

    if any(word in ticket for word in ["login", "crash", "error", "bug"]):
        return "Technical"

    return "Other"