#!/usr/bin/python

import sys


def output(previous_key, total):
    if previous_key is not None:
        print previous_key + " was found " + str(total) + " times"

previous_key = None
total = 0

for line in sys.stdin:
    key, value = line.split("\t",1)
    if key != previous_key:
        #if previous_key != None:
            #print previous_key + " was found" + str(total) +" time"
        output(previous_key, total)
        previous_key = key
        total = 0
    total = total + int(value)

#if previous_key != None:
#    print previous_key + " was found " + str(total) + " times"
output(previous_key, total)
