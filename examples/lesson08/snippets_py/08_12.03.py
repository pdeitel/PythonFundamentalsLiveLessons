# Section 8.12.3 snippets

### Function search—Finding the First Match Anywhere in a String
import re

result = re.search('Python', 'Python is fun')

result.group() if result else 'not found'

result2 = re.search('fun!', 'Python is fun')

result2.group() if result2 else 'not found'

### Ignoring Case with the Optional flags Keyword Argument
result3 = re.search('Sam', 'SAM WHITE', flags=re.IGNORECASE)

result3.group() if result3 else 'not found'

### Metacharacters that Restrict Matches to the Beginning or End of a String
result = re.search('^Python', 'Python is fun')

result.group() if result else 'not found'

result = re.search('^fun', 'Python is fun')

result.group() if result else 'not found'

result = re.search('Python$', 'Python is fun')

result.group() if result else 'not found'

result = re.search('fun$', 'Python is fun')

result.group() if result else 'not found'

### Function findall and finditer—Finding All Matches in a String
contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'

re.findall(r'\d{3}-\d{3}-\d{4}', contact)

for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(phone.group())

### Capturing Substrings in a Match
text = 'Charlie Cyan, e-mail: demo1@deitel.com'

pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'

result = re.search(pattern, text)

result.groups()

result.group()

result.group(1)

result.group(2)


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
