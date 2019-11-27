#!/bin/bash
string=onetwothreefour

#Extract substring 'three' and print
echo ${string:6:5}

#Remove substring 'one' and print
echo ${string#one}

#Remove substring 'four' and print
echo ${string%four}

#Replace substring 'four' with 'seven' and print
echo ${string/four/seven}
