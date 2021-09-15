"""Implementing the wc shell command in python."""

import sys#System Default library (line 8,11,14)

from lib.helper import wc, readfile # User Created Library to import user created functions

TEXT = None #Text is a variable assigned with a null value.
ARG_CNT = len(sys.argv) - 1 #ARG_CNT is a holding variable of returning value of a function call on Command Line Argument 

if ARG_CNT == 0: #Comparison Operators and If conditions
    TEXT = sys.stdin.read()# TEXT is a variable assigned to Input Reading

if ARG_CNT == 1:#Comparison Operators and If conditions
    filename = sys.argv[1]# filename is a variable assigned to Command line Argument 
    TEXT = readfile(filename)#TEXT is the holding variable of returning value of a function

response = wc(TEXT)#response is the holding variable of returning value of a function
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))#output function call or sys.stdout