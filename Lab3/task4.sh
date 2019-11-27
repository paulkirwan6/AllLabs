#!/bin/bash
# Write STDOUT (output of program/command) to file
ls -l > task4txt.txt
# Append STDOUT (output of program/command) to file
ls -l >> task4txt.txt
#Redirect stderr to an error file
ls /mnt/c/Users/Roshan George/Desktop/NUIG/Year 3/Sem 1/Embedded Systems Applications Programming/Assignments/Lab3 2> task4err.txt
#Redirect both stout and stderr to a file
ls &> both.txt
