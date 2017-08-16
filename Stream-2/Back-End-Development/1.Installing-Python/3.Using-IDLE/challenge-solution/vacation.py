def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    total_car = days * 40
    if days >= 7:
        total_car -= 50
    elif days >= 3:
        total_car -= 20
    return total_car

def trip_cost(city, days):
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days)

#invoke function here
print "The total cost for your trip comes to : ", trip_cost("Tampa", 7)
