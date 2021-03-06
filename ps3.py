#!/usr/bin/env python3
# Problem Set 3
# Sean Williams 
# 04-05-2022
import json
from math import gcd

# Helper Functions
def return_e(inDat):
    p = inDat["p"]
    q = inDat["q"]
    eList = []
    # Using notation from RSA module from NetSec
    phi = (p-1)*(q-1)
    for e in range(2, phi):
    # Check for greatest common denominator/ highest common factor
    # If the result is one then i is prime
    # Break on first value (per assignment)
        if gcd(e, phi) == 1:
            eList.append(e)
    return eList

def return_lcm(p, q):
    # Calculate lcm using gcd
    lcm = (p*q)//gcd(p,q)
    return lcm

def return_d(inDat, e):
    lcm = return_lcm((inDat["p"]-1),(inDat["q"]-1))
    for d in range(1, 10000):
        if ((d * e) % lcm) == 1:
            return d

# Problem 1
def problem1(inDat):
    prob1_res = []
    # Loop through input list
    numList = inDat["nums"]
    for i in numList:
        # Check each number for primality
        if i > 1:
            # Only need to check for i/2+1
            # Flag to pass to prime number append
            flag = True
            for j in range(2, int(i/2)+1):
                # No remainder = not prime
                if(i % j) == 0:
                    prob1_res.append(False)
                    flag = False
                    break
            if(flag):   
                prob1_res.append(True)   
    dictOut["problem 1"] = prob1_res
    return

# Problem 2
def problem2(inDat):
    dictOut["problem 2"] = return_e(inDat)[0]
    return 

# Problem 3
def problem3(inDat):
    # use help for lowest e
    e = return_e(inDat)[0]
    d = return_d(inDat, e)
    dictOut["problem 3"] = d
    return

# Problem 4
def problem4(inDat):
    dictOut["problem 4"] = (inDat["x"] ** inDat["e"]) % inDat["n"]
    return 

# Problem 5
def problem5(inDat):
    e = return_e(inDat)[0]
    n = inDat["p"] * inDat["q"]
    d = return_d(inDat, e)
    dictOut["problem 5"] = (inDat["y"] ** d) % n 
    return

# Read from file
input_test = open("example-input.json","r")
inputJSON = json.load(input_test)

dictOut = {
    "problem 1" : [],
    "problem 2" : "",
    "problem 3" : "",
    "problem 4" : "",
    "problem 5" : ""
}

# Problem Selection
for problemNum in inputJSON.keys():
    if(problemNum == "problem 1"): problem1(inputJSON[problemNum])
    elif(problemNum == "problem 2"): problem2(inputJSON[problemNum])
    elif(problemNum == "problem 3"): problem3(inputJSON[problemNum])
    elif(problemNum == "problem 4"): problem4(inputJSON[problemNum])
    elif(problemNum == "problem 5"): problem5(inputJSON[problemNum])
    else: exit()

json_submission = json.dumps(dictOut)
print(json_submission)