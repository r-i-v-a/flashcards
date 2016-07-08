#!/usr/bin/env python

import csv
import os
import random
import sys

divider = " : "

file_r = open(sys.argv[1], 'rU')
file_w = open("tmp.txt", 'w')
cards = file_r.readlines()

for c in cards:
    if divider not in c:
        continue
    file_w.write(c)

file_r.close()
file_w.close()
os.remove(sys.argv[1])
os.rename("tmp.txt", sys.argv[1])

file = open(sys.argv[1], 'rU')
cards = file.readlines()
file.close()
random.shuffle(cards)

print "\nq: quit program"
print "d: delete card"
print "\n+\n"
for c in cards:
    qa = c.split(divider)
    q = qa[0].strip()
    a = qa[1].strip()
    print q
    i = raw_input()
    print a
    i = raw_input()
    if i == 'q':
        print "[quit program]\n"
        break
    if i == 'd':
        print "[card deleted]\n"
        cards.remove(c)
    print "+\n"

file = open(sys.argv[1], 'w')
for c in cards:
    file.write(c)
file.close()
