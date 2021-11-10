#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Det är ett program som ber användaren mata in följande värden:

    Höjd över havet (meter)
    Hastighet (km/h)
    Temperatur utanför flygplanet (Celsius)

Sedan skall programmet skriva ut motsvarande värden enligt:

Höjd över havet (feet), 1 meter är 3.28084 feet.

Hastighet (mph), 1 kilometer är 0.62137 miles.

Temperatur utanför flygplanet (Farenheit)
För att konvertera från Celcius till Farenheit används följande formel:

[°F] = [°C] * 9 / 5 + 32
"""

# Ask the user to enter the height
# Assign the input string of the user to a variable

height_meter = input("Höjd över havet (meter): ")

# Convert the value to float type so can handle Mathematical operations
# Then convert it according to th program requirement
# And round it to two decimal.
# handle when an error occurs or exception

try:
    height_feet = round((float(height_meter) * 3.28084), 2)
except ValueError:
    height_meter = input("!!!!!!Skriv Höjd över havet (meter) med en heltal eller decimal !!!!!! ")
    height_feet = round((float(height_meter) * 3.28084), 2)


# Ask the user to enter the speed and assign it to a variable
speed_kmh = input("Hastighet (km/h): ")

# convert the value and round it

try:
    speed_mph = round((float(speed_kmh) * 0.62137), 2)
except ValueError:
    speed_kmh = input("!!!!!!Skriv Hastighet (km/h) med en heltal eller decimal !!!!!! ")
    speed_mph = round((float(speed_kmh) * 0.62137), 2)

# Ask the user to enter the temperature and assign it to a variable
temp_Celsius = input("Temperatur utanför flygplanet (Celsius): ")

# convert the value and round it
try:
    temp_Farenheit = round((float(temp_Celsius) * 9 / 5 + 32), 2)

except ValueError:
    temp_Celsius = input(
        "!!!!!!Skriv Temperatur utanför flygplanet (Celsius) med heltal eller decimal !!!!!! ")
    temp_Farenheit = round((float(temp_Celsius) * 9 / 5 + 32), 2)

# Print all converted values

print(
    f"Höjd över havet (feet):{height_feet}\nHastighet (mph): {speed_mph}\
        \nTemperatur utanför flygplanet (Farenheit): {temp_Farenheit}")
