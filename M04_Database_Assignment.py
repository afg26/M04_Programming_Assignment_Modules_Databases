#16.3 Create a CSV file called books2.csv by using these lines:
#created by the name os books2.CSV
"""
title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
"""

#Exercise #16.4 Use the sqlite3 module to create a SQLite database called books.db and a table called
# books with these fields: title (text), author (text), and year (integer).

#Creating our database
import sqlite3
connection = sqlite3.connect('books.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE books (title TEXT , author TEXT , year INTEGER)")


#16.5 Read books2.csv and insert its data into the book table.
#Opening our CSV file
with open('books2.csv', 'r') as my_file:
    for row in my_file:
        cursor.execute("insert into books values(?,?,?)", row.split(","))
    print("Data has been imported! ")
#Displaying our table
for row in cursor.execute("select * from books"):
    print(row)
connection.close()










