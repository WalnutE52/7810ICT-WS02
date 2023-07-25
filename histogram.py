import os
import sys
import string
lines = sys.stdin.readline()
key_values = {}
total = 0
while lines != "":
    line = lines.split()
    key = line[0]
    value = int(line[1])
    key_values[key] = value
    total += value
    lines = sys.stdin.readline()

for key, value in key_values.items():
    print(key.ljust(15), "\t [", sep="", end="")
    pre = int(value) * 100//total
    for i in range(0, pre, 5):
        print('*',sep="",end="")
    print(']',pre,'%',sep="")
    