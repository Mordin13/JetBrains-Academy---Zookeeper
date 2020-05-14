# put your python code here
duration = int(input())
food_cost_day = int(input())
one_way_flight_cost = int(input())
one_hotel_night_cost = int(input())

required_money = food_cost_day * duration + one_way_flight_cost * 2 + one_hotel_night_cost * (duration - 1)
print(required_money)