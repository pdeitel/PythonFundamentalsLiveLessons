# Section 6.2.4 snippets

months = {'January': 1, 'February': 2, 'March': 3}

for month_name in months.keys():
    print(month_name, end='  ')
    
for month_number in months.values():
    print(month_number, end='  ')
    
# Dictionary Views
months_view = months.keys()

for key in months_view:
    print(key, end='  ')

months['December'] = 12

months

for key in months_view:
    print(key, end='  ')

# Converting Dictionary Keys, Values and Key–Value Pairs to Lists
list(months.keys())

list(months.values())

list(months.items())

# Processing Keys in Sorted Order 

for month_name in sorted(months.keys()):
     print(month_name, end='  ')
     

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
