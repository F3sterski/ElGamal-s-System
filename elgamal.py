import sys
import random
from fractions import gcd

numbers_file = open("elgamal.txt", "r")
number1 = numbers_file.readline()
number2 = numbers_file.readline()
if number1 != "":
    number1 = long(number1)
if number2 != "":
    number2 = long(number2)

