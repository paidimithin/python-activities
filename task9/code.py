def monitor_hostel_resources():
    elec_rate = 8.0
    water_rate = 0.05
    elec_threshold = 150.0
    water_threshold = 2000.0

    hostel_data = {
        "Floor 1": {
            "Room 101": {"electricity": 120.0, "water": 1800.0},
            "Room 102": {"electricity": 160.0, "water": 2200.0}
        },
        "Floor 2": {
            "Room 201": {"electricity": 140.0, "water": 1700.0},
            "Room 202": {"electricity": 155.0, "water": 2100.0}
        }
    }

    floor_summary = {}

    print("--- ROOM-WISE RESOURCE MONITORING & CHARGES ---")
    for floor, rooms in hostel_data.items():
        floor_elec = 0.0
        floor_water = 0.0
        floor_cost = 0.0
        print(f"\n{floor}:")
        for room, metrics in rooms.items():
            e_con = metrics["electricity"]
            w_con = metrics["water"]
            
            e_cost = e_con * elec_rate
            w_cost = w_con * water_rate
            total_cost = e_cost + w_cost
            
            floor_elec += e_con
            floor_water += w_con
            floor_cost += total_cost
            
            violations = []
            if e_con > elec_threshold:
                violations.append("Electricity Exceeded")
            if w_con > water_threshold:
                violations.append("Water Exceeded")
            
            status = ", ".join(violations) if violations else "Normal"
            
            print(f"  {room} -> Elec: {e_con} kWh, Water: {w_con} L | Total Charge: ₹{total_cost:.2f} | Status: {status}")
        
        floor_summary[floor] = {
            "electricity": floor_elec,
            "water": floor_water,
            "cost": floor_cost
        }

    print("\n--- FLOOR-WISE UTILIZATION COMPARISON ---")
    for floor, summary in floor_summary.items():
        print(f"{floor} -> Total Electricity: {summary['electricity']} kWh | Total Water: {summary['water']} L | Total Cost: ₹{summary['cost']:.2f}")

if __name__ == "__main__":
    monitor_hostel_resources()
