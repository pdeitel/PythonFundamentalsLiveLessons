# Section 9.5 snippets

# JSON Data Format

# Python Standard Library Module `json` 
accounts_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

# Serializing an Object to JSON
import json

with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)

# Deserializing the JSON Text
with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)

accounts_json

accounts_json['accounts']

accounts_json['accounts'][0]

accounts_json['accounts'][1]

# Displaying the JSON Text
with open('accounts.json', 'r') as accounts:
    print(json.dumps(json.load(accounts), indent=4))
    





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
