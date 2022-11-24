from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "Let's drive!\n" \
       "q)uit, c)hoose taxi, d)rive"

# import taxis
available_taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

taxi = Taxi()
bill = 0.0

# menu sequence
print(MENU)
selection = input(">>> ").upper()
while selection != "Q":
    if selection == "C":
        # choose a taxi
        counter = 0
        print("Taxis available:")
        for available_taxi in available_taxis:
            print(f"{counter} - {available_taxi}")
            counter += 1
        try:
            taxi = available_taxis[int(input("Choose taxi: "))]
        except ValueError:
            print("Invalid taxi choice")
        except IndexError:
            print("Invalid taxi choice")
    elif selection == "D":
        # drive
        if taxi.name == "":
            print("You need to choose a taxi before you can drive")
        else:
            taxi.start_fare()
            try:
                taxi.drive(float(input("Drive how far? ")))
            except ValueError:
                print("Invalid distance")
            print(f"Your prius trip cost you ${taxi.get_fare():.2f}")
            bill += taxi.get_fare()
    else:
        print("Invalid option")
    # remove taxi from available list if out of fuel
    if taxi.fuel <= 0 and taxi.name != "":
        print("Your taxi has run out of fuel and is no longer available")
        available_taxis.remove(taxi)
        taxi = Taxi()
    print(f"Bill to date: ${bill:.2f}")
    print(MENU)
    selection = input(">>> ").upper()
print("Available taxis are now: ")
counter = 0
for available_taxi in available_taxis:
    print(f"{counter} - {available_taxi}")
    counter += 1
