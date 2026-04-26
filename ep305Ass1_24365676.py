# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:46:55 2026

@author: daire

Computes radiant flux of a blackbody using the Stefan-Boltzmann law for a 
range of values. The input values are in Fahrenheit, and specify the upper 
and lower bounds of the range.

X = 6
Y = 7
Z = 6
"""

from numpy import linspace

s = 5.670374419*10**-8 # Stefan-Boltzmann constant.

def toRadFlux(T):
    "Takes in a temperature and returns the radiant flux as a float."
    return s * T ** 4 # Stefan Boltzmann law


print("Range-based radiant flux calculator.")
print("""Please enter the two bounds of the range of temperatures 
      (in Fahrenheit) you want to calculate the fluxes for.""")
      
# Takes in two values as floats.
try:
    aFahrenheit = float(input("a = "))
    bFahrenheit = float(input("b = "))
except ValueError:
    raise ValueError(
        """At least one of the provided values was not able to be
        converted to a floating point number. Please check your
        inputs."""
                    )

# Converts the inputs to Kelvin.
a = (aFahrenheit - 32)/(9/5) + 273.15
b = (bFahrenheit - 32)/(9/5) + 273.15

# Checks that neither value is below absolute 0.
if a <= 0 or b <= 0:
    raise ValueError(
        """At least one provided values are below absolute 0 and 
        don't make physical sense. Please restart the program."""
        )
    
# Computes the maximum and minimum of the range.
maximum = max(a,b)
minimum = min(a,b)
    

# Prints the output values in a table.
print("\nComputed Values:")
print("-"*43)
print("| Temperature [K] | Radiant Flux [W m^-2] |")
for value in linspace(minimum, maximum, 75):
    flux = toRadFlux(value)
    print(f"| {value:<15.5} | {flux:<21.5} |")
print("-"*43)