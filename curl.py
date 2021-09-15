"""The python code helps to read the command line input for curl method."""

import sys #System Default library (line 7,13)
from lib.helper import curl # User Created Library to import user created functions

URL = None #URL is a variable assigned with a null value.
ARG_CNT = len(sys.argv) - 1#ARG_CNT is a holding variable of returning value of a function call on Command Line Argument 

if ARG_CNT != 1: #Comparison Operators and If conditions
    print('Usage: curl [URL]...')# output function call or sys.stdout


if ARG_CNT == 1:#Comparison Operators and If conditions
    URL = sys.argv[1] #URL is a variable assigned to Command line Argument 
    if 'http' not in URL[:5]:#Comparison Operators and If conditions
        URL = "http://"+URL#URL is a variable assigned to combining 2 variables or string
    print(curl(URL))#Multiple functions Call