try:  
    import mysql.connector
except ModuleNotFoundError as e:
    print(e)
    print("unfortunately your computer doesnt have the mysql.connecter module installed")
    print("try fixing this issue by installing the module")
    print("exiting the program")
    exit()
c=mysql.connector.connect(host="localhost",user="root",password="password",charset="utf8")
curs=c.cursor()
m=0
def end():
    print("thanks for using my program")
    exit()
 
def view():
    curs.execute("use test")
    curs.execute("select * from employeetest")
    table=curs.fetchall()                           #this program is used to see the employee table 
    for i in table:
        print(i)
    employeescreen()
def specview():
    try:
        curs.execute("use test")
        print("lets search for a product")
        print("type end to escape back to main menu")                #this program is used to search the whole table 
        print("enter the first few letter of your productname")      #for a product that starts with whatever you have inputted
        n=input(">>>")
        if n.lower()=="end":
            startcustomer()
        elif len(n)!=0:       
            curs.execute("select * from menutest where proname like'{}%'".format(n))
            
            table=curs.fetchall()
            if len(table)==0:
                print("there are no results for your search")
                print("lets try another seearch")
                specview()
            else:      
                for i in table:
                    print(i)
                print("this is all the available search results")
                print("going back to main menu")
                startcustomer()
        else:
            print("enter any character")                              #try exception block is used here to catch any errors and prevent the
                                                                    #the program from throwing an error and exiting the program unexpectedly
            specview()
    except Exception as e:
        print(f"sorry there has been an issue with your computer please try some other time")
        welcomescreen()      
def deleteemployee():
    curs.execute("use test")
    print("enter the admno of the person you want to delete")
    name=input(">>>")                                                                         #this function is used to delete an employee
    curs.execute("select admno,name,age from employeetest where admno={}".format(name))       #off a table with the help of their admno as a
    finite=curs.fetchall()                                                                    #identifier 
    print(f"are you sure you want to delete {finite} from this table ?")
    print("type y for yes")
    print("type n for no")
    print("type end to go back")                                                #used to confirm whether or not to delete it               
    choice=input(">>>")
    if choice.lower()=="end":
        print("moving back to main menu")
        startscreen()
    elif choice.lower()=="y":
        print(f"deleting {finite} from the database of employees")
        curs.execute("delete from employeetest where admno={}".format(name))
        c.commit()
        print(f"succesfully deleted {finite} from the database")
        print("would you like to delete more or return back to main menu")
        print("type y for yes")                                                 #used to return to the same program to delete more members if needed
        print("type n for no")
        supra=input(">>>")
        if supra.lower()=="n":
            print("moving back to main menu")
            employeescreen()
        elif supra.lower()=="y":
            print("continuing the process of removing more members")
            deleteemployee()
    elif choice.lower()=="n":
        print("lets enter new values")
        deleteemployee()
    else:
        print("please enter a valid option (either y , n or end.)")
        deleteemployee()
def viewmenu():
    curs.execute("use test")
    curs.execute("select * from menutest")                                      #used to view the customer table
    table=curs.fetchall()
    for i in table:
        print(i)
    startcustomer()
def checker():   
    print("is this the first time initiating this program ?")                 
    print("type y for yes and n for no")                                        #this program is used to install the databases and start a table
    choice=input(">>>")                                                         #try exception block is used to catch any error such as the database
    try:                                                                        #already being installed or, the tables already exists.
        if choice=="y":
            curs.execute("create database test")
            curs.execute("use test")
            curs.execute("create table menutest(sino varchar(8),proname varchar(20),price varchar(6),producer varchar(15), batchno varchar(10))") 
            curs.execute("create table employeetest(admno varchar(5),name varchar(20),phoneno varchar(20),sex varchar(4),age varchar(3))")        
            c.commit()
            print("congrats on purchasing our program.")
            print("installation of our program is complete please proceed to the main program")
            welcomescreen()  
        elif choice=="n":
            print("please use the other program")
            welcomescreen()
        else:
          print("please type an actual value")
          checker()    
    except mysql.connector.errors.DatabaseError as e:
        print("the database that you are trying to add already exists in the computer")
        welcomescreen()     
def insertfood():
    curs.execute("use test")
    nott=0
    print("Alright... lets add a new product")
    print()                                                     #this is a program used to add a new product into the customer
    print("Here's the present list of products")                #products table
    curs.execute("select * from menutest")
    print("TYPE END TO GO BACK TO THE MAIN MENU")
    table=curs.fetchall()
    for x in table:
        print(x)  
    print("enter a sino")
    n1=input(">>>")                       #first input(sino)
    if n1.lower()=="end":
        print("command detected, moving to MAIN MENU")
        startcustomer()
    elif n1.isdigit()==False:
        print("try using your brain and enter a proper number ?")
        insertfood()
    print("enter the proname")
    n2=input(">>>")                       #second input(proname)
    if n2.lower()=="end":
        print("command detected, moving to MAIN MENU")
        customerscreen()  
    print("enter the sale price")         #third input(price)
    n3=input(">>>")
    if n3.lower()=="end":
        print("command detected, moving to MAIN MENU")
        customerscreen()
    elif n3.isdigit()==False:
            print("try entering a proper phone ?")
            insertfood()
    print("enter producer")                   #fourth input(producer)
    n4=input(">>>")
    if n4.isalpha()==False:
        print(f"enter a name please")
        insertfood()
    print("enter the batchno ")                     #fifth input(batchno)
    n5=input(">>>")
    if n5.lower()=="end":
        print("command detected, moving to MAIN MENU")
        customerscreen()
    elif n5.isdigit()==False:
        print("try and enter a proper number ?")
        insertfood()
    curs.execute("insert into menutest values('{}','{}','{}','{}','{}')".format(n1,n2,n3,n4,n5))
    c.commit()
    curs.execute("select * from menutest")
    results=curs.fetchall()
    for i in results :
        print(i)
    print("process done")
    print("do you want to enter more products")
    print("for adding more products type y")
    print("for continuing back to main menu type n")
    print("for going back type end")
    choice=input(">>>")
    if choice.lower()=="end":
        print("moving to main menu")
        customerscreen() 
    elif choice.lower()=="y":
        print("lets add more products then")
        insertfood()
    elif choice.lower()=="n":
        print("exiting to main menu")
        customerscreen()
    else :
        print("please enter a alphabetical value(either end, y or n)")
        insertfood()
def welcomescreener():
    print("+--------------------------------------------------------------+")
    print("|        WELCOME TO SPORTWORLD                                 |")
    print("+--------------------------------------------------------------+")
    print("                                                                ")
    print("+--------------------------------------------------------------+")    #this is the starting program 
    print("| where customers come to fulfil their shopping needs          |")
    print("+--------------------------------------------------------------+")
    print("| Select profile                                               |")    #welcome screen
    print("+------------------------------------+-------------------------+")
    print("| Customer                           | TYPE 1                  |")
    print("| Retailer                           | TYPE 2                  |")
    print("| install SPORTWORLD.in              | TYPE 3                  |")
    print("| end this whole program             | TYPE end                |")
    print("+------------------------------------+-------------------------+")
    print()
    print("enter your choice")
    choice=input(">>>")
    if choice.lower()=="end":
        end()
    elif choice=="1":
        startcustomer()
    elif choice=="2":
        employeescreen()
    elif choice=="3":
        checker()
    else:
        print("please enter a number")
        welcomescreener()
def welcomescreen():
    print("+--------------------------------------------------------------+")
    print("|        WELCOME TO SPORTWORLD                                 |")
    print("+--------------------------------------------------------------+")
    print("                                                                ")
    print("+--------------------------------------------------------------+")
    print("| where customers come to fulfil their sports needs            |")
    print("+--------------------------------------------------------------+")
    print("| Select profile                                               |")    #welcome screen
    print("+------------------------------------+-------------------------+")
    print("| Customer                           | TYPE 1                  |")    #this is the screen you will see once the application is already installed
    print("| Retailer                           | TYPE 2                  |")
    print("| end this whole program             | TYPE end                |")
    print("+------------------------------------+-------------------------+")
    print()
    print("enter your choice")
    choice=input(">>>")
    choicer=choice.lower()
    if choicer=="end":
        end()
    elif choice=="1":
        startcustomer()
    elif choice=="2":
        employeescreen()
    else:
        print("please enter a number")
        welcomescreen()
def priceview():
    curs.execute("use test")
    curs.execute("select * from menutest order by price asc")           #this function is used to sort all the items by price
    table=curs.fetchall()
    for i in table:
        print(i)
    startcustomer()   
def employeesearch():
    curs.execute("use test")
    print("type end to escape back to main menu")
    print("")
    print("enter the first few letter of your employeename")            #this function is used to search an employee by its name
    n=input(">>>")
    if n.lower()=="end":
        startscreen()
    curs.execute("select * from employeetest where name like'{}%'".format(n))
    table=curs.fetchall()
    if len(table)==0:
        print("there are no results for your search")
        print("lets try another search")
        employeesearch()
    elif len(table)!=0:      
        for i in table:
            print(i)
        print("this is all the available search ")
        print("would you like to search another type y or n or end")
        xender=input(">>>")        
        if xender.lower()=="end":
            print("moving to employee menu")
            employeescreen()           
        elif xender.lower()=="y":
            print("lets search a new employee")
            employeesearch()
        elif xender.lower()=="n":
            print("moving to employee menu")
            employeescreen()  
        else:
            print("moving to employee menu")
            employeescreen()
def startcustomer():
    print("+--------------------------------------------------------------+")
    print("|        WELCOME TO SPORTWORLD (customer edition)              |")
    print("+--------------------------------------------------------------+")
    print("                                                                ")
    print("+--------------------------------------------------------------+")    #this is the customer version of the application 
    print("| WHAT DO YOU NEED HELP WITH ?                                 |")
    print("+-----------------------------------+--------------------------+")    #customer version
    print("| View product list                 | TYPE 1                   |")
    print("| Search for a product              | TYPE 2                   |")
    print("| view product by pricing           | TYPE 3                   |")
    print("| Go back to welcome screen         | TYPE 4                   |")
    print("| Exit program                      | TYPE end                 |")
    print("+-----------------------------------+--------------------------+")
    print("enter your choice")
    choice=input(">>>")
    digit=choice.isdigit()
    if choice=="end":
        print("moving to welcome screen")
        welcomescreen()
    elif digit==False:
        print("PLEASE ENTER A NUMBER")
        startcustomer()
    elif choice=="1":                                      #first viewing product list
        print("heres the list of all products")
        viewmenu()
    elif choice=="2":                                      #second searching for a product
        specview()
    elif choice=="3":                                      #third viewing in asc order
        print("here is the product list in the ascending order")
        priceview()
    elif choice=="4":                                      #fourth going back to welcome screen
        welcomescreen()
    elif choice=="5":                                      #fifth exiting the program
        exit()
    else:
        print("please enter a valid option either end y,n")
        startcustomer()
def employeescreen():
    print("+--------------------------------------------------------------+")
    print("|        WELCOME TO HYPERMARKET MAX (Retailer edition)         |")
    print("+--------------------------------------------------------------+")
    print("                                                                ")
    print("+--------------------------------------------------------------+")
    print("| WHAT DO YOU NEED HELP WITH ?                                 |")
    print("+-----------------------------------+--------------------------+")   #employee version
    print("| Add employees                     | TYPE 1                   |")   #this menu has much more administrative control
    print("| View employee list                | TYPE 2                   |")   
    print("| Delete an employee with admno     | TYPE 3                   |")
    print("| Search an employee with name      | TYPE 4                   |")
    print("| go back to the welcome screen     | TYPE 5                   |")
    print("| end this whole program            | TYPE 6                   |")
    print("| add an item into the product list | TYPE 7                   |")    
    print("+-----------------------------------+--------------------------+")
    print()
    print("enter your choice")
    choice=input(">>>")
    digit=choice.isdigit()
    if digit==False:
        
        print("PLEASE ENTER A NUMBER")
        startscreen()
    elif choice=="1":                                                          
        addpeople()
        #add  employee
    elif choice=="2":
        print("Here's the present employee table")                             #view employee list
        view()
        
    elif choice=="3":
        print("lets delete an employee from the database")                     #deleting employee
        deleteemployee()
        
    elif choice=="4":
        print("lets search an employee")                      #searching an employee with name
        employeesearch()
        
    elif choice=="5":
        welcomescreen()
        
    elif choice=="6":
        c=1
        end()

    elif choice=="7":
        insertfood()
        
    else:
        print("please enter a valid option")
        startscreen()
        
welcomescreener()                                         #this calls and starts the whole program
