from classifier import classify_ticket

ticket = input("Enter Support Ticket: ")

category = classify_ticket(ticket)

print("\nCategory:", category)