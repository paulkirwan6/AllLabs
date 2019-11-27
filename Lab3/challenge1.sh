#!/bin/bash
echo "please enter a password"
read pass
VAR=lenVal
VAR=charVal

if (( ${#pass} >= 10)); then
        echo "yaaay"
        lenVal=true
else
        echo "password must be atleast 10 characters!!"
        lenVal=false
fi

if (( ${pass:0:4} == "pass" )); then
        echo ${pass:0:4}
        echo "password cant start with \"pass\""
        charVal=false
else
        echo "thanks for not using \"pass\""
        charVal=true
fi

if [[ "$lenVal" == true && "$charVal" == true ]]; then
        echo "good password. saved"
        echo "$password > password_saved.txt"
        chmod 400 password_saved.txt
else
        echo "weak password"
fi
