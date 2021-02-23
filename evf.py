import os
import subprocess
import sys, string, os
import termcolor
import time as wait
def scansql(input):
    os.system("cls")
    print("Start Finder...")
    os.system("python scansql/scanqli.py -u "+input)
def req():
    os.system("cls")
    print("Install Requirements...")
    os.system("start req.bat")
def basicdos():
    os.system("cls")
    print("Starting Attack...")
    os.system("python serverstress/ddos.py")
def banner():
    print("""
███████╗ █████╗ ███████╗██╗   ██╗    ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ██║   ██║██║   ██║██║     ████╗  ██║    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ███████║███████╗ ╚████╔╝     ██║   ██║██║   ██║██║     ██╔██╗ ██║    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████╗██║  ██║███████║   ██║        ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝         ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                          
Easy Vuln Finder[Developing yet...]
redhackaze.org | MyPoison
""")
count = 1
os.system("cls")
while True:
    yesorno = input("""
███████╗ █████╗ ███████╗██╗   ██╗    ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ██║   ██║██║   ██║██║     ████╗  ██║    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ███████║███████╗ ╚████╔╝     ██║   ██║██║   ██║██║     ██╔██╗ ██║    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██╔══██║╚════██║  ╚██╔╝      ╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████╗██║  ██║███████║   ██║        ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝         ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                          
Easy Vuln Finder[Developing yet...]
redhackaze.org | MyPoison
The developers who make this application do not accept any responsibility. Do you accept my terms(Y/N) ? \n \neasyvuln > """)
    if yesorno == "y" or yesorno == "Y" or yesorno == "yes" or yesorno == "YES":
        os.system("cls")
        while(count<2):
            banner()   
            a =  input("""\n1)Collecting information from the server.
2)Offensive Vuln analysis from target server.
3)For download requirements(If you have not installed the requirements, you must install the requirements)
4)Server Stress(DDOS etc.)
5)Commands

easyvuln > """)
            if a == "home":
                os.system("cls")
                continue
            elif a == "quit":
                sys.exit()
            elif a == "1":
                os.system("cls")
                banner()
                selectattack = input("\n1)Nmap Analysis \n2)Automatic Analysis \neasyvuln > ")
                count2 = 1
                while(count2<2):
                    if selectattack == "quit":
                        sys.exit()
                    elif selectattack == "home":
                        os.system("cls")
                        count2 +=1
                    elif selectattack == "1":
                        os.system("python NMAP/nmapinterface.py")
                    elif selectattack == "2":
                        print("Developing yet...")
                        continue
                    else:
                        os.system("cls")
                        wait.sleep(2)
                        print("Wrong Argument")
                        continue
            elif a == "2":
                os.system("cls")
                banner()
                selectattack = input("\n1) Offensive Vuln With SQLMAP \n2)SQLI Vuln Scanner \n3)Automatic Attack \neasyvuln > ")
                
                count2 = 1
                while(count2<2):
                    if selectattack == "quit":
                        sys.exit()
                    elif selectattack == "home":
                        os.system("cls")
                        count2 +=1
                    elif selectattack == "1":
                        os.system("cls")
                        os.system("python sqlmap/sqlinterface.py")
                    elif selectattack == "2":
                        os.system("cls")
                        target = input("Enter The Target | easyvuln > ")
                        scansql(target)
                    else:
                        os.system("cls")
                        wait.sleep(2)
                        print("Wrong Argument")
                        continue
            elif a == "3":
                req()
            elif a == "4":
                count2 =1
                os.system("cls")
                while(count2<2):
                    banner()

                    select = input("1)Basic Dos Atatck 2)Comming Later...")
                    if select == "home":
                        count2 +=1
                    elif select == "quit":
                        sys.exit()
                    elif select == "1":
                        basicdos()
                    elif select == "2":
                        print("Not ready yet(. Coming later...")
                    elif select == "3":
                        os.system("cls")
                        continue
                
                    else:
                        print("Wrong Argument")
                        wait.sleep(2)
                        os.system("cls")
                        continue
            elif a == "5":
                print("""
        For back to main page : "home"
        For quit of tool : "quit"        
        """)
            else:
                os.system("cls")
                print("Wrong Argument")
                wait.sleep(2)
                os.system("cls")
                continue
    elif yesorno == "quit":
        sys.exit()
    elif yesorno == "home":
        print("You not use from here")
        wait.sleep(2)
        os.system("cls")        
    else:
        print("You must accept of terms for you use to tool")
        wait.sleep(2)
        os.system("cls")
        continue


            
             






    


