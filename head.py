"""Implementing the head shell command in python."""

import sys#System Default library (line 7,10,13)
from lib.helper import head, readfile # User Created Library to import user created functions

TEXT = None #Text is a variable assigned with a null value.
ARG_CNT = len(sys.argv) - 1 #ARG_CNT is a holding variable of returning value of a function call on Command Line Argument 

if ARG_CNT == 0:#Comparison Operators and If conditions
    TEXT = sys.stdin.read()# TEXT is a variable assigned to Input Reading

if ARG_CNT == 1:#Comparison Operators and If conditions
    filename = sys.argv[1]# filename is a variable assigned to Command line Argument 
    TEXT = readfile(filename)#TEXT is the holding variable of returning value of a function

if ARG_CNT > 1:#Comparison Operators and If conditions
    print("Usage: head.py <file>")# output function call or sys.stdout

print(head(TEXT))#Multiple functions Call