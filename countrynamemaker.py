# extremely scuffed and very stupid. shows that i have no life
import random

names = []

numnames = int(input("How many names do you want? "))
maxlength = int(input("What is the maximum length of the names? "))//3

for x in range(numnames):
    countryname = ""
    for i in range(random.randint(1, maxlength)):
        choice = random.choice("abcdefghijklmnopqrstuvwyz")
        countryname += choice
        if choice != "a" and choice != "e" and choice != "i" and choice != "o" and choice != "u":
            choice = random.choice("aeiou")
            countryname += choice
        choice = random.choice("bcdfghjklmnpqrstvwyz")
        countryname += choice
    names.append(countryname)

for i in names:
    print(i)