# Section 16.3 snippets 

# Tables, Rows and Columns

# Selecting Data Subsets

# SQLite

# 16.3.1 A books Database

# Creating the books Database

# Connecting to the Database in Python
import sqlite3

connection = sqlite3.connect('books.db')

# authors Table

# Viewing the authors Table’s Contents
import pandas as pd

pd.options.display.max_columns = 10

pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])

# titles Table
pd.read_sql('SELECT * FROM titles', connection)

# author_ISBN Table
df = pd.read_sql('SELECT * FROM author_ISBN', connection)

df.head()

# Entity-Relationship (ER) Diagram

# SQL Keywords

# 16.3.2 SELECT Queries
pd.read_sql('SELECT first, last FROM authors', connection)

# 16.3.3 WHERE Clause
pd.read_sql("""SELECT title, edition, copyright 
                FROM titles 
                WHERE copyright > '2016'""", connection)

# Pattern Matching: Zero or More Characters 
pd.read_sql("""SELECT id, first, last 
                FROM authors 
                WHERE last LIKE 'D%'""", 
             connection, index_col=['id'])
              
# Pattern Matching: Any Character
pd.read_sql("""SELECT id, first, last 
                FROM authors 
                WHERE first LIKE '_b%'""", 
             connection, index_col=['id'])
              
# 16.3.4 ORDER BY Clause
pd.read_sql('SELECT title FROM titles ORDER BY title ASC',
             connection)

# Sorting By Multiple Columns
pd.read_sql("""SELECT id, first, last 
                FROM authors 
                ORDER BY last, first""", 
             connection, index_col=['id'])

pd.read_sql("""SELECT id, first, last 
                FROM authors 
                ORDER BY last DESC, first ASC""", 
             connection, index_col=['id'])
              
# Combining the WHERE and ORDER BY Clauses
pd.read_sql("""SELECT isbn, title, edition, copyright
                FROM titles
                WHERE title LIKE '%How to Program'
                ORDER BY title""", connection)

# 16.3.5 Merging Data from Multiple Tables: INNER JOIN
pd.read_sql("""SELECT first, last, isbn
                FROM authors
                INNER JOIN author_ISBN
                    ON authors.id = author_ISBN.id
                ORDER BY last, first""", connection).head()

# 16.3.6 INSERT INTO Statement
cursor = connection.cursor()

cursor = cursor.execute("""INSERT INTO authors (first, last)
                            VALUES ('Sue', 'Red')""")

pd.read_sql('SELECT id, first, last FROM authors', 
             connection, index_col=['id'])
             
# Note Regarding Strings That Contain Single Quotes

# 16.3.7 UPDATE Statement
cursor = cursor.execute("""UPDATE authors SET last='Black'
                            WHERE last='Red' AND first='Sue'""") 

cursor.rowcount

pd.read_sql('SELECT id, first, last FROM authors', 
             connection, index_col=['id'])
             
# 16.3.8 DELETE FROM Statement
cursor = cursor.execute('DELETE FROM authors where id=6') 

cursor.rowcount

pd.read_sql('SELECT id, first, last FROM authors', 
             connection, index_col=['id'])

# Closing the Database
connection.close()

# SQL in Big Data

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
