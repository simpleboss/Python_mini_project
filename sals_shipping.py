def get_cost_of_ground_shipping(weight):
    cost = 20
    if weight <= 2:
        per_pound = 1.5
    elif weight <= 6:
        per_pound = 3 
    elif weight <= 10:
        per_pound = 4
    else:
        per_pound = 4.75
    return cost + per_pound * weight

cost_of_premium_ground_shipping = 125

#print(cost_of_ground_shipping(8.4))

def get_cost_of_drone_shipping(weight):
    cost = 0
    if weight <= 2:
        per_pound = 4.5
    elif weight <= 6:
        per_pound = 9 
    elif weight <= 10:
        per_pound = 12
    else:
        per_pound = 14.25
    return cost + per_pound * weight

#print(cost_of_drone_shipping(1.5))

def get_best_way_of_shipping(weight):
    if (cost_of_premium_ground_shipping <= get_cost_of_drone_shipping(weight) and
    cost_of_premium_ground_shipping <= get_cost_of_ground_shipping(weight) ):
        result_of_way_of_shipping = 'Premium Ground shipping'
        result_of_price = cost_of_premium_ground_shipping
    elif(get_cost_of_drone_shipping(weight) <= get_cost_of_ground_shipping(weight)):
        result_of_way_of_shipping = 'Drone shipping'
        result_of_price = cost_of_drone_shipping(weight)
    else:
        result_of_way_of_shipping = 'Ground shipping'
        result_of_price = get_cost_of_ground_shipping(weight)    
    print('The best way of shipping :'+result_of_way_of_shipping) 
    print('The price                :'+str(result_of_price))  

get_best_way_of_shipping(4.8)
print('=====')
get_best_way_of_shipping(41.5)