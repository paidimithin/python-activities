def evaluate_basket(budget, items, discount_threshold, discount_rate):
    basket = [item.copy() for item in items]
    
    def calculate_total(current_basket):
        subtotal = sum(item['price'] * item['quantity'] for item in current_basket)
        if subtotal > discount_threshold:
            return subtotal * (1 - discount_rate)
        return subtotal

    total_cost = calculate_total(basket)
    
    while total_cost > budget:
        basket.sort(key=lambda x: x['price'], reverse=False)
        reduced = False
        for item in basket:
            if item['quantity'] > 0:
                item['quantity'] -= 1
                reduced = True
                break
        if not reduced:
            break
        total_cost = calculate_total(basket)
        
    return basket, total_cost

budget = 500.0
items = [
    {'name': 'Laptop', 'price': 400.0, 'quantity': 1},
    {'name': 'Mouse', 'price': 50.0, 'quantity': 2},
    {'name': 'Keyboard', 'price': 100.0, 'quantity': 1}
]
discount_threshold = 400.0
discount_rate = 0.10

final_basket, final_cost = evaluate_based := evaluate_basket(budget, items, discount_threshold, discount_rate)
print("Final Basket:", final_basket)
print("Final Cost:", final_cost)
