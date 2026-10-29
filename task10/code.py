def audit_festival(participants_data, sponsorships, expenses):
    unique_participants = {}
    duplicates = 0
    
    for p in participants_data:
        pid = p["id"]
        if pid in unique_participants:
            duplicates += 1
        else:
            unique_participants[pid] = p
            
    total_reg_revenue = sum(p["fee"] for p in unique_participants.values())
    total_sponsorship = sum(s["amount"] for s in sponsorships)
    total_expenses = sum(e["amount"] for e in expenses)
    
    net_balance = (total_reg_revenue + total_sponsorship) - total_expenses
    
    return {
        "total_unique_participants": len(unique_participants),
        "duplicate_registrations": duplicates,
        "total_registration_revenue": total_reg_revenue,
        "total_sponsorship": total_sponsorship,
        "total_expenses": total_expenses,
        "final_balance": net_balance
    }

if __name__ == "__main__":
    participants = [
        {"id": "P001", "name": "Alice", "fee": 500},
        {"id": "P002", "name": "Bob", "fee": 500},
        {"id": "P001", "name": "Alice", "fee": 500},
        {"id": "P003", "name": "Charlie", "fee": 600}
    ]
    
    sponsorships = [
        {"sponsor": "TechCorp", "amount": 15000},
        {"sponsor": "LocalCafe", "amount": 5000}
    ]
    
    expenses = [
        {"item": "Stage Setup", "amount": 6000},
        {"item": "Sound System", "amount": 4000}
    ]
    
    result = audit_festival(participants, sponsorships, expenses)
    for key, value in result.items():
        print(f"{key}: {value}")
