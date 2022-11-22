from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi(50, "Taxi", 2)
taxi.drive(18)
print(f"{taxi.get_fare():.2f}")
