#!/bin/bash
#if no user input is given, use a default value
echo "what is your name?"; read name
echo "your name is ${name:-No One}"
