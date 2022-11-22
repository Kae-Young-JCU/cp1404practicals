from car import Car
from taxi import Taxi

my_taxi = Taxi(100, "Prius 1")
my_taxi.drive(40)
print(f"{my_taxi}. Fair is {my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"Fair is {my_taxi.get_fare()}")
