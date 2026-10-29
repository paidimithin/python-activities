def calculate_cost(plan, usage):
    base = plan["base_price"]
    
    excess_min = max(0, usage["minutes"] - plan["inc_minutes"])
    excess_data = max(0, usage["data"] - plan["inc_data"])
    excess_sms = max(0, usage["sms"] - plan["inc_sms"])
    
    excess_charges = (
        excess_min * plan["rate_min"] +
        excess_data * plan["rate_data"] +
        excess_sms * plan["rate_sms"]
    )
    
    return base + excess_charges

def find_best_plan(plans, usage, budget):
    best_plan = None
    min_cost = float("inf")
    
    for plan in plans:
        total_cost = calculate_cost(plan, usage)
        if total_cost <= budget and total_cost < min_cost:
            min_cost = total_cost
            best_plan = plan
            
    return best_plan, min_cost

if __name__ == "__main__":
    user_usage = {
        "minutes": 350,
        "data": 12.5,
        "sms": 100
    }
    max_budget = 600.0
    
    available_plans = [
        {
            "name": "Plan A",
            "base_price": 300.0,
            "inc_minutes": 300,
            "inc_data": 10.0,
            "inc_sms": 50,
            "rate_min": 1.5,
            "rate_data": 15.0,
            "rate_sms": 0.5
        },
        {
            "name": "Plan B",
            "base_price": 500.0,
            "inc_minutes": 500,
            "inc_data": 20.0,
            "inc_sms": 200,
            "rate_min": 1.0,
            "rate_data": 10.0,
            "rate_sms": 0.2
        },
        {
            "name": "Plan C",
            "base_price": 400.0,
            "inc_minutes": 400,
            "inc_data": 15.0,
            "inc_sms": 100,
            "rate_min": 1.2,
            "rate_data": 12.0,
            "rate_sms": 0.4
        }
    ]
    
    best, cost = find_best_plan(available_plans, user_usage, max_budget)
    
    if best:
        print(f"Optimal Plan: {best['name']}")
        print(f"Total Cost: {cost}")
    else:
        print("No eligible plan found within the budget.")
