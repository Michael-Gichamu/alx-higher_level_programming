#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
string = "Last digit of {} is {} and is".format(number, last_digit)
if last_digit > 5:
    print(string, "greater than 5")
elif last_digit == 0:
    print(string, "0")
else:
    print(string, "less than 6 and not 0")
