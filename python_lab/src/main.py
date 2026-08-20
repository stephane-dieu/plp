#!/usr/bin/env python3

from utils import *

def main():
   
      num = int(input("enter a number pls: "))

      sq_val = square(num)
      even_odd_val = is_even(num)
      f_val = celsius_to_fahrenheit(num)

      name = input("type your name please: ")
      greet(name)

      print(f"Square: {sq_val}")
      print(f"Parity: {even_odd_val}")
      print(f"Fahrenheit equivalent: {f_val}°F")


if __name__== "__main__":
      main()
