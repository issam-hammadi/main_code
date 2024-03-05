#tutorial of freecodecamp
import sqlite3

def show_all():
    #Query all DB and return all records 
    conn = sqlite3.connect("customer1.db")
    c = conn.cursor() #create a cursor instance 
    c.execute('SELECT rowid, * FROM customers1')
    items = c.fetchall()
    print("Name " + "\t\tEMAIL")
    print("-----" + "\t\t" + "-------")
    for item in items: 
        print(item)
    conn.commit()

    #Close our connection
    conn.close()
#Add a new record to the table 
def add_one(first, last, email): 
    conn = sqlite3.connect("customer1.db")
    c = conn.cursor() #create a cursor instance 

    c.execute("INSERT INTO customers1 VALUES (?,?,?)", (first, last, email))
    conn.commit()

    #Close our connection
    conn.close()

#delete a record
def delete_record(id):
    conn = sqlite3.connect("customer1.db")
    c = conn.cursor() #create a cursor instance 
    c.execute("DELETE from customers1 WHERE rowid = (?)", id)
    conn.commit()

    #Close our connection
    conn.close()

#add many records 
def add_many_records(list):
    conn = sqlite3.connect("customer1.db")
    c = conn.cursor() #create a cursor instance 

    c.executemany("INSERT INTO customers1 VALUES (?,?,?)", list)
    conn.commit()

    #Close our connection
    conn.close()

#Where clause function 
def email_lookup(email):
    conn = sqlite3.connect("customer1.db")
    c = conn.cursor() #create a cursor instance 

    c.execute("SELECT * from customers1 WHERE email = (?)", (email,))
    items = c.fetchall()
    print("Name " + "\t\tEMAIL")
    print("-----" + "\t\t" + "-------")
    for item in items: 
        print(item)
    conn.commit()

    #Close our connection
    conn.close()


# creating a data base in the memory 
# conn = sqlite3.connect(":memory:")

#creating a connection with sqlite3 or connecting it if it already exists
#conn = sqlite3.connect("customer1.db")

#c = conn.cursor() #create a cursor instance 

# Inserting data into the table 
#c.execute("INSERT INTO customers1 VALUES ('Issam' , 'HAMMADI', 'issamhammadi@gmail.com')")

#Inserting many values at the same time
#many_customers = [('Wes','Brown', 'wes@brown.com'),
                 #('Steph', 'kuewa', 'steph@gmail.com'),
                 #('hafsa', 'elboudrissi', 'hafsaelboudrissi@gmail.com') 
                 #]

#c.executemany("INSERT INTO customers1 VALUES (?,?,?)", many_customers)
#create a table 

#c.execute(""" CREATE TABLE customers1 (
#    first_name text,
#    last_name text,
#    email text
#)""")
#
#Query the database
#Ordering results 
#c.execute('SELECT rowid, * FROM customers1 ORDER BY last_name DESC')
#and / or 
#c.execute("SELECT rowid, * FROM customers1 WHERE last_name LIKE 'HAM%' OR  rowid = 3")
#Limiting records
#c.execute("SELECT rowid, * FROM customers1 ORDER BY rowid DESC  LIMIT 2 ")
#Delete an entire table / drop the table 
#c.execute("DROP TABLE customers1")
#delete record 
#c.execute("DELETE from customers1 WHERE rowid = 4")
#Update a record

#c.execute("""UPDATE customers1 SET first_name = 'Issam'
          #WHERE rowid = 1
#""") #I tis better to use rowid, because we could have a lot of hammadi's 


#c.execute("SELECT rowid, * FROM customers1")
#Where clause 
#c.execute("SELECT * FROM customers1 WHERE email LIKE '%gmail.com' ")


#Primary key : another column, each row has its own ID 


    

#print(c.fetchone()[0])
#print(c.fetchmany(3))
#print(c.fetchall())
#print("command executed successsfully")

#Formatting the results 

#DATATTYPES
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#Commit our command
#conn.commit()


