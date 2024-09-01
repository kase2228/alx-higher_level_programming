#!/usr/bin/python3
import random
string = random.randint(-10000, 10000)
string = str(string)
if int(string[-1]) > 5:
    print("Last digit of " + str(string) + " is "
          + str(string[-1]) + " and is greater than 5")
elif int(string[-1]) == 0:
    print("Last digit of " + str(string)
          + " is " + str(string[-1]) + " and is 0")
elif int(string[-1]) < 6 and string[-1] != 0:
    print("Last digit of " + str(string)
          + " is " + str(string[-1]) + " and is less than 6 and not 0")
