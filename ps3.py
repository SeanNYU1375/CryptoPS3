#!/usr/bin/env python3
# Problem Set 2
# Sean Williams 
# 04-05-2022
import json

# Problem 1
def problem1():
    return []

# Problem 2
def problem2():
    return 0

# Problem 3
def problem3():
    return 0

# Problem 4
def problem4():
    return 0

# Problem 5
def problem5():
    return 0


# read from stdin
#assignmentIn = sys.stdin
#inputJSON = json.load(assignmentIn)

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