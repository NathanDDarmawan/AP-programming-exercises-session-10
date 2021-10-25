def calc_weight_on_planet(weight, gravity=23.1):
    new_weight = (weight/9.8)*gravity
    return new_weight

print(calc_weight_on_planet(120,23.1))
