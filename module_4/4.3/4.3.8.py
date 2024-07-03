MILE = 1609.344  # metres
GALLON = 3.785411784  # liters


def liters_100km_to_miles_gallon(liters):
    return (GALLON * 100000) / (liters * MILE)


def miles_gallon_to_liters_100km(miles):
    return (GALLON * 100000) / (miles * MILE)


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
