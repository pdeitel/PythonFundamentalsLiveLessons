# Section 9.3.2 Self Check snippets

# Exercise 3
with open('grades.txt', 'r') as grades:
    print(f'{"ID":<4}{"Name":<7}{"Grade"}')
    for record in grades:  
        student_id, name, grade = record.split()
        print(f'{student_id:<4}{name:<7}{grade}')
        


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
