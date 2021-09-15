"""Implementing the tac shell command in python."""

import sys#System Default library (line 7,10,13,17)
from lib.helper import tac, readfile # User Created Library to import user created functions

TEXT = None #Text is a variable assigned with a null value.
ARG_CNT = len(sys.argv) - 1 #ARG_CNT is a holding variable of returning value of a function call on Command Line Argument 

if ARG_CNT == 0:#Comparison Operators and If conditions
    TEXT = sys.stdin.read()# TEXT is a variable assigned to Input Reading 

if ARG_CNT == 1:#Comparison Operators and If conditions
    filename = sys.argv[1]# filename is a variable assigned to Command line Argument 
    TEXT = readfile(filename)#TEXT is the holding variable of returning value of a function 

if ARG_CNT > 1:#Comparison Operators and If conditions
    print(sys.argv[0], "doesn't handle more than one argument") # output function call or sys.stdout

print(tac(TEXT))#Multiple functions Call