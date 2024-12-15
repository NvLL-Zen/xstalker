import platform
import subprocess
import os
import geocoder
import re
import scapy.all as scapy

def detect_os():
    system_name = platform.system()
    if system_name == "Windows":
        return "cls"
    elif system_name == "Linux":
        return "clear"
    else:
       return "clear"

def clear_terminal():
    os.system(clear_command)


if __name__ == "__main__":
    clear_command = detect_os()
    print(clear_command)
    clear_terminal()

    welcome_message = """
 __   __ _____ _        _ _             
 \ \ / // ____| |      | | |            
  \ V /| (___ | |_ __ _| | | _____ _ __ 
   > <  \___ \| __/ _` | | |/ / _ \ '__|
  / . \ ____) | || (_| | |   <  __/ |   
 /_/ \_\_____/ \__\__,_|_|_|\_\___|_|    

 XStalker by nvll-zen

 For list of commands, type 'help'                                      
"""

    help_message = """
-------------------
Commands    | Info
-------------------
locate ip


"""

    print(welcome_message)
    while True:
        prompt = input(" ~> ")
        print(prompt)

        if prompt == "exit":
            print(" Exiting...")
            exit()
        if prompt == "help":
            print("help")
        if prompt == "locate ip":
            print("please specify user address")
            ip_addr = input(" ~> ")
            geodata = geocoder.ip(ip_addr)
            print("\n")
            print(f"[+] IP: {ip_addr}")
            print(f"[+] Coordinates: {geodata.latlng}")
            print(f"[+] City:  {geodata.city}")
            print(f"[+] State/Province: {geodata.state}")
            print(f"[+] Postal Code:  {geodata.postal}")
            print(f"[+] Country:  {geodata.country}")
            print(f"[+] ASN/Org: {geodata.org}")
            print("\n")
        if prompt == "lookup ip":
            print("\n")
            nspinp = input(" ?> ")
            nspcmd = subprocess.run(['nslookup', '-type=a', nspinp], shell=True)
            print(nspcmd)
            print("\n")
        if prompt == "arping":
            print("\n")
            ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
            print("Please input ip range")
            ip_range = input(" ?> ")
            if ip_add_range_pattern.search(ip_range):
                print(f"{ip_range} is a valid ip address range")
                arp_result = scapy.arping(ip_range)
            else:
                print("Incrorrect input,(example:192.xxx.x.x/24")
    
    
