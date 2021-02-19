import os
import subprocess
import sys, string, os
import termcolor

count = 1




os.system("cls")
while(count<2):

    print("""______                 __      __    _          ______ _           _
 |  ____|                \ \    / /   | |        |  ____(_)         | |
 | |__   __ _ ___ _   _   \ \  / /   _| |_ __    | |__   _ _ __   __| | ___ _ __
 |  __| / _` / __| | | |   \ \/ / | | | | '_ \   |  __| | | '_ \ / _` |/ _ \ '__|
 | |___| (_| \__ \ |_| |    \  /| |_| | | | | |  | |    | | | | | (_| |  __/ |
 |______\__,_|___/\__, |     \/  \__,_|_|_| |_|  |_|    |_|_| |_|\__,_|\___|_|
                   __/ |
                  |___/    \/
Easy Vuln Finder[Developing yet...]
By redahackaze.org MyPoison | ig: @yusuf.ngs    \n """)
    keyboard = input("The developers who make this application do not accept any responsibility. Do you accept my terms(Y/N) ? \n \neasyvuln > ")
    if(keyboard == "Y" or keyboard == "y" or keyboard == "yes" or keyboard == "YES"):
        while True:
            select = input("""\n1)Collecting information from the server.
2)Offensive Vuln analysis from target server.
3)For download requirements(If you have not installed the requirements, you must install the requirements)
4)Server Stress(DDOS etc.)
5)For Exit

easyvuln > """)
            if(select == "1"):
                #deneme için
                selectattack = input("\n1)Nmap Analysis \n2)Automatic Analysis \n3)for exit \n \neasyvuln > ")
                count2 = 1
                while(count2<2):
                    if(selectattack == "1"):
                        os.system("python nmap/nmapinterface.py")
                    elif(selectattack == "3"):
                        print("Process stoped...")
                        count2 += 1
                    else:
                        print("Try again. Wrong choice")


            elif(select == "3"):
                print("installing requirements....")
                os.system("start req.bat")



            elif(select == "2"):
                selectattack = input("\n1) Offensive Vuln With SQLMAP \n2)SQLI Vuln Scanner \n3)Automatic Attack \n4)for exit \n \neasyvuln > ")
                count2 = 1
                while(count2<2):
                    if(selectattack == "1"):

                        os.system("python easyvulnmod.py")
                        count2 += 1
                    elif(selectattack == "2"):
                        target = input("Enter the target(you must use the http/https) easyvuln > ")
                        os.system("python scansql\scanqli.py -u "+target)
                        count2 += 1
                    elif(selectattack == "4"):
                        count2 += 1


                #deneme için

            elif(select == "5"):
                count += 1
                break
            elif(select == "4"):
                os.system("python serverstress/ddos.py")



            else:
                print("Enter correct argument")
    elif(keyboard != "Y"):
        print("You can't use it without accepting")
        break

print("\nSee you , bye :)")
