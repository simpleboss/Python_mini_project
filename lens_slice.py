# Task 1
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies',
            'mushrooms']

# Task 2
prices = [2, 6, 1, 3, 2, 7, 2]

# Task 3
num_pizzas = len(toppings)

# Task 4
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

# Task 5
pizzas = list(zip(prices, toppings))

# Task 6
print(pizzas)

# Task 7
pizzas.sort()

# Task 8
cheapest_pizza = pizzas[0]

# Task 9
priciest_pizza = pizzas[-1]

# Task 10
three_cheapest = pizzas[:3]

# Task 11
print(three_cheapest)

# Task 12
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)