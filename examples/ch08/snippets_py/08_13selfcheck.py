# Section 8.13 Self Check snippets

# Exercise 2
import pandas as pd

import re

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
            ['Sue Brown', 'demo2@deitel.com', '5555551234']]

contactsdf = pd.DataFrame(contacts, 
                          columns=['Name', 'Email', 'Phone'])

def get_formatted_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    if result:
        part1, part2, part3 = result.groups()
        return '(' + part1 + ') ' + part2 + '-' + part3
    else:       
        return value

contactsdf['Phone'] = contactsdf['Phone'].map(get_formatted_phone)

contactsdf






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
