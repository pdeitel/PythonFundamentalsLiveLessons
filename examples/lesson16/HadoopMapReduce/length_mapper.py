#!/usr/bin/env python3
# length_mapper.py
"""Maps lines of text to key-value pairs of word lengths and 1."""
import sys

def tokenize_input():
    """Split each line of standard input into a list of strings."""
    for line in sys.stdin:
        yield line.split()

# read each line in the the standard input and for every word 
# produce a key-value pair containing the word, a tab and 1
for line in tokenize_input():
    for word in line:
        print(str(len(word)) + '\t1')

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
