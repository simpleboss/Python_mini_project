def cost_of_ground_shipping(weight):
    cost = 20
    if weight <= 2:
        cost += 1.5 * weight
    elif weight <= 6:
        cost += 3 * weight 
    elif weight <= 10:
        cost += 4 * weight
    else:
        cost += 4.75 * weight
    return cost

cost_of_premium_ground_shipping = 125

#print(cost_of_ground_shipping(8.4))

def cost_of_drone_shipping(weight):
    cost = 0
    if weight <= 2:
        cost += 4.5 * weight
    elif weight <= 6:
        cost += 9 * weight 
    elif weight <= 10:
        cost += 12 * weight
    else:
        cost += 14.25 * weight
    return cost

#print(cost_of_drone_shipping(1.5))

def best_way_of_shipping(weight):
    if (cost_of_premium_ground_shipping <= cost_of_drone_shipping(weight) and
    cost_of_premium_ground_shipping <= cost_of_ground_shipping(weight) ):
        result_of_way_of_shipping = 'Premium Ground shipping'
        result_of_price = cost_of_premium_ground_shipping
    elif(cost_of_drone_shipping(weight) <= cost_of_ground_shipping(weight)):
        result_of_way_of_shipping = 'Drone shipping'
        result_of_price = cost_of_drone_shipping(weight)
    else:
        result_of_way_of_shipping = 'Ground shipping'
        result_of_price = cost_of_ground_shipping(weight)    
    print('The best way of shipping :'+result_of_way_of_shipping) 
    print('The price                :'+str(result_of_price))  

best_way_of_shipping(4.8)
print('=====')
best_way_of_shipping(41.5)