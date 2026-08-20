#!/usr/bin/env python3

from utils import *

def main():

      num = int(input("enter a number pls: "))

      sq_val = square(num)
      even_odd_val = is_even(num)
      f_val = celsius_to_fahrenheit(num)

      even_odd_str = "even" if even_odd_val else "odd"


      print(f"Square: {sq_val}")
      print(f"Parity: {even_odd_val}")
      print(f"even or odd: {even_odd_str} ")
      print(f"Fahrenheit equivalent: {f_val}°F")


if __name__=="__main__":
      main()
