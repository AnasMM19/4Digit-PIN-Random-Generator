from itertools import count
import random


print("Enter the number of PINs to generate: ")
NumberOfPIN = int(input())

AllPINs = random.sample(range(1000,9999), NumberOfPIN)

print(AllPINs)