# Section 11.5 snippets
# Loading the Language Model

import spacy

nlp = spacy.load('en') 

# Creating a spaCy Doc
document = nlp('In 1994, Tim Berners-Lee founded the ' + 
    'World Wide Web Consortium (W3C), devoted to ' +
    'developing web technologies')
    
# Getting the Named Entities
for entity in document.ents:
    print(f'{entity.text}: {entity.label_}')
    



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
