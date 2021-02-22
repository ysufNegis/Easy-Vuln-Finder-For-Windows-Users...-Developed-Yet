import os , sys , string
import time as wait

#Classes
def fastscan(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe "+input)

def verscan(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -sV "+input)

def agrscan(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -A "+input)

def tcpscan(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -sT "+input)

def udpscan(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -sU "+input)

def vulnscan(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -sU "+input)

def banner():
    print("""
███╗   ██╗███╗   ███╗ █████╗ ██████╗     ███████╗ █████╗ ███████╗██╗   ██╗    ██╗   ██╗  ███████╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ██║   ██║  ██╔════╝
██╔██╗ ██║██╔████╔██║███████║██████╔╝    █████╗  ███████║███████╗ ╚████╔╝     ██║   ██║  █████╗  
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     ██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ╚██╗ ██╔╝  ██╔══╝  
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         ███████╗██║  ██║███████║   ██║        ╚████╔╝██╗██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝         ╚═══╝ ╚═╝╚═╝     
redhackaze.org | MyPoison                                                                                               """)

def owner():
    print("redhackaze.org | My Poison")

def wafbypass(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe --script firewall-bypass "+input)

def topports(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe --top-ports 30 "+input)

def osservice(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -A -T4 "+input)

def slowloris(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -max-parallelism 800 -Pn --script http-slowloris --script-args http-slowloris.runforever=true "+input)

def malscan(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -sV --script=http-malware-host "+input)

def httpenum(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -n -p 80 --script http-enum "+input)

def vulnscan(port,input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -sV "+port+" --script=vulscan/vulscan "+input)

def dnsbrute(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -p80 --script dns-brute "+input)

def httpconfig(input):
    os.system("cls")
    print("Start Scannning...")
    wait.sleep(4)
    os.system("nmap.exe -n -p80 --script http-config-backup "+input)
def clear(input):
	os.system("cls")
def traceroute(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe --traceroute "+input)
def tcpnull(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -sN "+input)
def xmasscan(input):
    os.system("cls")
    print("Start Scanning...")
    wait.sleep(4)
    os.system("nmap.exe -sN "+input)
count = 1

os.system("cls")

while(count<2):
    print("""
███╗   ██╗███╗   ███╗ █████╗ ██████╗     ███████╗ █████╗ ███████╗██╗   ██╗    ██╗   ██╗  ███████╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ██║   ██║  ██╔════╝
██╔██╗ ██║██╔████╔██║███████║██████╔╝    █████╗  ███████║███████╗ ╚████╔╝     ██║   ██║  █████╗  
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     ██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ╚██╗ ██╔╝  ██╔══╝  
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         ███████╗██║  ██║███████║   ██║        ╚████╔╝██╗██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝         ╚═══╝ ╚═╝╚═╝     
 redhackaze.org | MyPoison                                                                                                 """)
    
    
    

    a = input("""
1)Easy Scanning
2)Version Scanning
3)Agresive Scanning
4)Only TCP Scanning
5)Only UDP Scanning
6)Vulnerability Scanning(CVE Searching)
7)Traceroute
8)TCP NULL Scan
9)Xmas Scan
10)Extra Categories
11)Commands

easyvuln > """)
    
    if(a =="1"):
        target = input("Target Web Site | easyvuln > ")        
        if(target == "quit"):
            sys.exit()
        elif(target == "home"):
            os.system("cls")
            continue
        else:
            fastscan(target)
        

    elif(a == "2"):
        target = input("Target Web Site | easyvuln > ")
        if(target == "quit"):
            sys.exit()
        elif target == "home":
            os.system("cls")
            continue
        else:
            verscan(target)
        
    elif(a =="3"):
        target = input("Target Web Site | easyvuln > ")
        if target == "quit":
            sys.exit()
        elif target == "home":
            os.system("cls")
            continue
        else:
            agrscan(target)

    elif a == "4":
        target = input("Target Web Site | easyvuln > ")
        if target == "quit":
            sys.exit()
        elif target == "home":
            os.system("cls")
            continue
        else:
            tcpscan(target)

    elif a == "5":
        target = input("Target Web Site | easyvuln > ")
        if target == "quit":
            sys.exit()
        elif target == "home":
            os.system("cls")
            continue
        else:
            udpscan(target)
    elif a == "6":
        target = input("Target Web Site | easyvuln > ")
        if target == "quit":
            sys.exit()
        elif(target == "home"):
            os.system("cls")
            continue
        else:
            udpscan(target)
    elif a == "10":
        os.system("cls")
        count2 = 1
        while(count2<2):

            print("""
███╗   ██╗███╗   ███╗ █████╗ ██████╗     ███████╗ █████╗ ███████╗██╗   ██╗    ██╗   ██╗  ███████╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ██║   ██║  ██╔════╝
██╔██╗ ██║██╔████╔██║███████║██████╔╝    █████╗  ███████║███████╗ ╚████╔╝     ██║   ██║  █████╗  
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     ██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ╚██╗ ██╔╝  ██╔══╝  
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         ███████╗██║  ██║███████║   ██║        ╚████╔╝██╗██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝         ╚═══╝ ╚═╝╚═╝     
 redhackaze.org | MyPoison                                                                                                 """)
    
            b = input("""
1)Advanced Scan For Servers With Waf
2)Advanced Scripts
3)Only Scan on Top Ports
4)OS Service Detection
5)Dos Attack With Nmap(SlowLoris)
6)Malware Detecting On Server
easyvuln > """)
            if(b == "1"):
                if(b == "quit"):
                    sys.exit()
                elif b == "home":
                    count2+=1
                else:
                    target = input("Target Web Site | easyvuln > ")  
                    wafbypass(target)
            elif(b == "2"):
                if b == "quit":
                    sys.exit()
                elif b == "home":
                   
                     count2+=1
                else:
                    
                    count3 =1
                    os.system("cls")
                    while(count3<2):
                        print("""
███╗   ██╗███╗   ███╗ █████╗ ██████╗     ███████╗ █████╗ ███████╗██╗   ██╗    ██╗   ██╗  ███████╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ██║   ██║  ██╔════╝
██╔██╗ ██║██╔████╔██║███████║██████╔╝    █████╗  ███████║███████╗ ╚████╔╝     ██║   ██║  █████╗  
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     ██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ╚██╗ ██╔╝  ██╔══╝  
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         ███████╗██║  ██║███████║   ██║        ╚████╔╝██╗██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝         ╚═══╝ ╚═╝╚═╝     
 redhackaze.org | MyPoison                                                                                                 """)
                        
                        inputs = input("""
1)Http Enum (Profesoniel Index Scanning)
2)Vulnscan (Advanced Detecting Vuln on Server)
3)Dns Brute (Subdomain Scanner)
4)Http Config (Dump Web Site Config)
easyvuln > """)
                        if inputs == "1":
                            target = input("Target Web Site | easyvuln > ")
                            if target == "quit":
                                sys.exit()
                            elif(target == "home"):
                                count2+=1
                                count3+=1
                            else:
                                httpenum(target)

                        elif inputs == "2":
                            target = input("Target Web Site | easyvuln > ")
                            if target == "quit":
                                sys.exit()
                            elif target == "home":
                                count2+=1
                                count3+=1
                            else:
                                selectport = str(input("Select Port | easyvuln > "))
                                if selectport == "quit":
                                    sys.exit()
                                elif selectport == "home":
                                    count2 +=1
                                    count3 +=1
                                else:
                                    vulnscan(selectport,target)

                        elif inputs == "3":
                            target = input("Target Web Site | easyvuln > ") 
                            if target == "quit":
                                sys.exit()
                            elif target == "home":
                                count2+=1
                                count3+=1
                            else:
                                dnsbrute(target)
                        elif inputs =="4":
                            target = input("Target Web Site | easyvuln > ")
                            if target == "quit":
                                sys.exit()
                            elif target == "home":
                                count2+=1
                                count3+=1
                            else:
                                httpconfig(target)
                        #devam
                        elif inputs == "quit":
                            sys.exit()
                        elif inputs == "home":
                            count2+=1
                            count3+=1
                        elif inputs == "banner":
                            banner()




                        else:
                            print("Invalid Select")
                        
            elif(b == "3"):
                if b == "quit":
                    sys.exit()
                elif b == "home":
                    os.system("cls")
                    count2+=1
                else:
                    target = input("Target Web Site | easyvuln > ")  
                    topports(target)
                

            
            elif(b=="4"):
                target = input("Target Web Site | easyvuln > ")  
                if target =="quit":
                    sys.exit()
                elif target =="home":
                    os.system("cls")
                    count2+=1
                else:
                    osservice(target) 
                
            elif(b == "5"):
                target = input("Target Web Site | easyvuln > ")  
                if target == "quit":
                    sys.exit()
                elif target == "home":
                    os.system("cls")
                    count2 +=1
                else:
                    slowloris(target)
                

            elif b == "6":
                target = input("Target Web Site | easyvuln > ")  
                if target == "quit":
                    sys.exit()
                elif target == "home":
                    os.system("cls")
                    count2+=1
                else:
                    malscan(target)
                
            elif b == "quit":
                sys.exit()
            elif b == "home":
                os.system("cls")
                count2 +=1
            elif b =="banner":
                banner()
            elif b == "owner":
                owner()
            else:
                print("Invalid Select")

    elif a == "7":
        target = input("Target Web Site | easyvuln > ") 
        if target == "quit":
            sys.exit()
        elif target == "home":
            os.system("cls")
            continue
        else:
            traceroute(target)
    elif a == "8":
        target = input("Target Web Site | easyvuln > ") 
        if target == "quit":
            sys.exit()
        elif target == "home":
            os.system("cls")
            continue
        else:
            tcpnull(target)
    elif a == "9":
        target = input("Target Web Site | easyvuln > ") 
        if target == "quit":
            sys.exit()
        elif target == "home":
            os.system("cls")
            continue
        else:
            xmasscan(target)





            
    elif a == "11":
        os.system("cls")
        print("""
For Exit : "quit" 
For go main page : "home" 
For banner : "banner" 
For owner : "owner" 
""")
        wait.sleep(2)
        


        
    elif a == "quit":
        sys.exit()
    elif a == "banner":
        banner()
    elif a == "owner":
        print("redhackaze.org | My Poison")
    else:
        print("Invalid select")
print("See you bye...")
