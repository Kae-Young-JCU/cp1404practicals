from prac_06.guitar import Guitar

a = Guitar("Gibson L-5 CES", 1922, 16035.4)
b = Guitar("Another Guitar", 2013)


print(f"{a.name} get_age() - Expected 100. Got {a.get_age()}")
print(f"{b.name} get_age() - Expected 9. Got {b.get_age()}")
print(f"{a.name} is_vintage() - Expected True. Got {a.is_vintage()}")
print(f"{b.name} is_vintage() - Expected False. Got {b.is_vintage()}")
