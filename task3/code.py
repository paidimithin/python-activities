import math

def main():
    venue_cost = float(input("Enter venue cost: "))
    equipment_cost = float(input("Enter equipment cost: "))
    transport_cost = float(input("Enter transport cost: "))
    catering_per_person = float(input("Enter catering cost per person: "))
    certificate_per_person = float(input("Enter certificate cost per person: "))
    fee_per_person = float(input("Enter participant contribution per person: "))
    total_sponsorship = float(input("Enter total sponsorship amount: "))
    expected_participants = int(input("Enter expected number of participants: "))

    total_fixed_cost = venue_cost + equipment_cost + transport_cost
    variable_cost_per_person = catering_per_person + certificate_per_person
    
    total_cost = total_fixed_cost + (variable_cost_per_person * expected_participants)
    total_revenue = (fee_per_person * expected_participants) + total_sponsorship
    
    shortfall = total_cost - total_revenue
    
    net_contribution_per_person = fee_per_person - variable_cost_per_person
    if net_contribution_per_person > 0:
        numerator = total_fixed_cost - total_sponsorship
        min_break_even = math.ceil(numerator / net_contribution_per_person)
        if min_break_even < 0:
            min_break_even = 0
    else:
        min_break_even = "Infinity (Contribution does not cover variable costs)"

    print("\n--- Event Financial Summary ---")
    print(f"Total Fixed Cost: ${total_fixed_cost:.2f}")
    print(f"Variable Cost Per Person: ${variable_cost_per_person:.2f}")
    print(f"Total Expected Cost: ${total_cost:.2f}")
    print(f"Total Expected Revenue: ${total_revenue:.2f}")
    if shortfall > 0:
        print(f"Financial Shortfall: ${shortfall:.2f}")
    else:
        print(f"Financial Surplus: ${abs(shortfall):.2f}")
    print(f"Minimum Break-Even Registration Count: {min_break_even}")

if __name__ == "__main__":
    main()
