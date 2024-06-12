print('############################################  Query Ease  ###############################################')


######################################### HIDDEN ###########################################
cn = True
cd = False
while cn == True:
    try :
        passwd = input('Enter password : ')
        import mysql.connector
        conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = passwd, database = '')
        mycursor = conn.cursor()
        cn = False
        cd = True
    except:
        print('INVALID PASSWORD :-(')
        choice = input('Enter do you want to retry(y/n) : ')
        if choice.lower() == 'y':
            cn = True
        else:
            cn = False
############################################################################################
    
    
########################################## FUNCTIONS #######################################
def open_database():
    C_OPEN = True
    while C_OPEN == True:
        try:
            database = input('Enter name of database : ')
            conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = passwd, database = database)
            mycursor = conn.cursor()
            command = 'use '+ database
            mycursor.execute(command)
            print()
            print('$$$$$$$$$$$$$   Database opened    $$$$$$$$$$$$$')
            print()
            table_options(database)
            
            C_OPEN = False
        except:
            print("UNKOWN DATABASE :-( ")
            choice = input('Enter do you want to retry(y/n) : ')
            if choice.lower() == 'y':
                C_OPEN = True
            else:
                C_OPEN = False
                
def quitsql():
    print('BYE')
    return False




def table_options(database):
    print('   CHOICE')
    print('          1. Show all tables')
    print('          2. Create table ')
    print('          3. Describe table (table structure)')
    print('          4. See table data')
    print('          5. Delete table')
    print('          6. Insert value in table')
    print('          7. Custom query')
    print('          8. Back')
    
    choice = input('Enter your choice : ')
    if choice == '1':
        show_tables(database)
    elif choice == '2':
        create_table(database)
    elif choice == '3':
        desc_see_delete_table(choice,database) 
    elif choice == '4':
        desc_see_delete_table(choice,database)
    elif choice == '5':
        desc_see_delete_table(choice,database)
    elif choice == '6':
        table_name = input('Enter table name : ')
        conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', database = database)
        mycursor = conn.cursor()
        command = 'desc '+ table_name
        mycursor.execute(command)
        data = mycursor.fetchall()
        datavalue = []
        for i in data:
             print('Enter value for ',i[0],end = '')
             value = input(' : ')
             if value.isdigit():
                 value = int(value)
                 datavalue.append(value)
             else:
                datavalue.append(value)
        datavalue = tuple(datavalue)
        datavalue = str(datavalue)
        command = 'insert into '+ table_name + ' values' + datavalue
        mycursor.execute(command)
        conn.commit()
        print('$$$$$$$$$$$ Data inserted $$$$$$$$$$$$')
        table_options(database)
    elif choice == '7':
        custom_query(database)
    elif choice == '8':
        pass

                 
             
        
        
    

def desc_see_delete_table(choice,database):
    try:
        table_name = input('Enter table name : ')
        conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', database = database)
        mycursor = conn.cursor()
        if choice == '3':        
            command = 'desc '+ table_name
            mycursor.execute(command)
            data = mycursor.fetchall()
            for i in data:
                print(i)
            table_options(database)
        elif choice =='4':
            command = 'select * from '+ table_name
            mycursor.execute(command)
            data = mycursor.fetchall()
            for i in data:
                print(i)
            table_options(database)
        elif choice == '5':
            command = 'drop table '+ table_name
            mycursor.execute(command)
            conn.commit()
            print('$$$$$$$$$$$ Table Deleted $$$$$$$$$$$')
            table_options(database)
            

            
    except:
        print('This table is not present in your database',database)
        ch = input('Do you want to retry?(y/n) : ')
        if ch.lower() == 'y':
            desc_see_delete_table(choice, database)
        else:
            table_options(database)
            
            


def custom_query(database):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', database = database)
    mycursor = conn.cursor()
    command = input('Enter mysql query : ')
    mycursor.execute(command)
    try:
        conn.commit()
        print('$$$$$$$$$$$  DONE  $$$$$$$$$$$$')
        table_options(database)
    except :
        data = mycursor.fetchall()
        for i in data:
            print(i)
        print()
        table_options(database)

            
            
            
            
            
            
            
def create_table(database):
    conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', database = database)
    mycursor = conn.cursor()
    table_name = input('Enter name of table : ')
    noc = input('Enter number columns : ')
    lst =[]
    if noc.isdigit():
        for i in range(1,int(noc)+1):
            row = input('Enter name of column (with datatype and constraints) : ')
            lst.append(row)
    else:
        print('Enter valid number')
                
                
    c = 'create table ' + table_name + '('
    for i in range(len(lst)):
        if i<len(lst)-1:
            c = c + lst[i] + ','
        else:
            c = c + lst[i]
    
    
    c = c + ')'

    try:
        mycursor.execute(c)
        conn.commit()
        print('Table created')
        table_options(database)
    except:
        print(''''invalid query
                  - Enter correct datatype and their values within limits''')


    
def show_tables(database):
    print()
    print('$$$$$$$$$$$$$$   ALL TABLES   $$$$$$$$$$$$$$')
    print()
    conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = passwd, database = database)
    mycursor = conn.cursor()
    mycursor.execute('show tables')
    data = mycursor.fetchall()
    for i in data:
        print(i)
    print()
    table_options(database)



def create_db():
    db_name = input('Enter name of database : ')
    command = 'create database '+ db_name
    mycursor.execute(command)
    print('$$$$$$$$$$$$$$   DATABASE CREATED   $$$$$$$$$$$$$$')
    cd = True
    while cd:
        print()
        print('   CHOICE')
        print('          1. See all databases ')
        print('          2. Open a database ')
        print('          3. Create new database')
        print('          4. Delete database')
        choice = input('Enter your choice : ')
        if choice == '1':
            print()
            print('$$$$$$$$$$$$$$   ALL DATABASES   $$$$$$$$$$$$$$')
            print()

            mycursor.execute('show databases')
            data = mycursor.fetchall()
            for i in data:
                print(i)
            
        elif choice == '2':
            open_database() 
        elif choice == '3':
            create_db()
        elif choice == '4':
            delete_db()
        else:
            print('INVALID CHOICE :-( ' )
            retry = input('Do you want to retry?(y/n) : ' )
            if retry.lower() =='y':
                cd = True
            else:
                cd = False
    
        cd = False
        
def delete_db():
    db_name = input('Enter name of database : ')
    command ='drop database '+ db_name
    mycursor.execute(command)
    print('$$$$$$$$$$$$ Database deleted $$$$$$$$$$$$$')

    
    

    
###################################################################################################   
print()
print('$$$$$$$$$$$$$$   ACCESS GRANTED   $$$$$$$$$$$$$$')
while cd:

    print()
    print('   CHOICE')
    print('          1. See all databases ')
    print('          2. Open a database ')
    print('          3. Create new database')
    print('          4. Delete database')
    print('          5. Custom query')
    print('          6. Quit')
    choice = input('Enter your choice : ')
    if choice == '1':
        print()
        print('$$$$$$$$$$$$$$   ALL DATABASES   $$$$$$$$$$$$$$')
        print()

        mycursor.execute('show databases')
        data = mycursor.fetchall()
        for i in data:
            print(i)
    elif choice == '2':
        open_database() 
    elif choice == '3':
        create_db()
    elif choice == '4':
        delete_db()
    elif choice == '5':
        database = input('Enter name of database(if any) : ')
        custom_query(database)
    elif choice == '6':
        cd = quitsql()
    else:
        print('INVALID CHOICE :-( ' )
        retry = input('Do you want to retry?(y/n) : ')
        if retry.lower() == 'y':
            cd = True
        else:
            cd = False
    
    
    

    