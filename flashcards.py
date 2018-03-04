#!/usr/bin/env python

import csv
import os
import random
import sys

divider = " = "

file_r = open(sys.argv[1], 'rU')
file_w = open("x.txt", 'w')
cards = file_r.readlines()

random.shuffle(cards)

for c in cards:
    if divider not in c:
        continue
    file_w.write(c)

file_r.close()
file_w.close()
os.remove(sys.argv[1])
os.rename("x.txt", sys.argv[1])

file = open(sys.argv[1], 'rU')
cards = file.readlines()
file.close()

print("\n/ press q to quit /")
print("\n.\n")

for c in cards:
    card = c.split(divider)

    print(card[0].strip())
    i = input()
    if i == 'q':
        break

    print(card[1].strip())
    i = input()
    if i == 'q':
        break

    print(".\n")