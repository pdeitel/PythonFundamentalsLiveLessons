# Section 8.9 Self Checksnippets

# Exercise 2
', '.join(reversed('Pamela White'.split()))

# Exercise 3
url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'

protocol, separator, rest_of_url = url.partition('://')

host, separator, document_with_path = rest_of_url.partition('/')

host

path, separator, document = document_with_path.rpartition('/')

path


    


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
