# Section 8.9 snippets

# Splitting Strings
letters = 'A, B, C, D'

letters.split(', ')

letters.split(', ', 2)

# Joining Strings
letters_list = ['A', 'B', 'C', 'D']

','.join(letters_list)

','.join([str(i) for i in range(10)])

# String Methods partition and rpartition 
'Amanda: 89, 97, 92'.partition(': ')

url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'

rest_of_url, separator, document = url.rpartition('/')

document

rest_of_url

# String Method splitlines 
lines = """This is line 1
This is line2
This is line3"""

lines

lines.splitlines()

lines.splitlines(True)


    

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
