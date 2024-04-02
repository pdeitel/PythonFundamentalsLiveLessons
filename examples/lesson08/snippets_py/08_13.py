# Section 8.13 snippets

# Cleaning Your Data 

# Data Validation
import pandas as pd

zips = pd.Series({'Boston': '02215', 'Miami': '3310'})

zips

zips.str.match(r'\d{5}')

cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])

cities

cities.str.contains(r' [A-Z]{2} ')

cities.str.match(r' [A-Z]{2} ')

# Reformatting Your Data

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
            ['Sue Brown', 'demo2@deitel.com', '5555551234']]

contactsdf = pd.DataFrame(contacts, 
                          columns=['Name', 'Email', 'Phone'])

contactsdf

import re

def get_formatted_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return '-'.join(result.groups()) if result else value

formatted_phone = contactsdf['Phone'].map(get_formatted_phone)

formatted_phone

contactsdf['Phone'] = formatted_phone

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
