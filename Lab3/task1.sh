#!/bin/bash
string=hello
echo "string: $string"
echo "string length = ${#string}"
# alternative method
echo "alternative method: string length = `expr length $string`"
#you can also get the length of an integer variable
num1=9
num2=999
echo "length of $num1 = ${#num1}"
echo "length of $num2 = ${#num2}"
