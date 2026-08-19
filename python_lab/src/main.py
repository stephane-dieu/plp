#!/usr/bin/env python3

from utils.py import *

def main():
   try:
      num = int(input("enter a number pls: "))

      sq_val = square(num)
      even_odd_val = is_even(num)
      f_val = celsius_to_fahrenheit(num)


      print(f"Square: {sq_val}")
      print(f"Parity: {even_odd_val}")
      print(f"Fahrenheit equivalent: {f_val}°F")

   except ValueError:
        print("Please enter a valid numeric value.")

