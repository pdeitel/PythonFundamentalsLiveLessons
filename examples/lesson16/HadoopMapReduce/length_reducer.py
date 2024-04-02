#!/usr/bin/env python3
# length_reducer.py
"""Counts the number of words with each length."""
import sys
from itertools import groupby
from operator import itemgetter

def tokenize_input():
    """Split each line of standard input into a key and a value."""
    for line in sys.stdin:
        yield line.strip().split('\t')

# produce key-value pairs of word lengths and counts separated by tabs
for word_length, group in groupby(tokenize_input(), itemgetter(0)):
    try:
        total = sum(int(count) for word_length, count in group)
        print(word_length + '\t' + str(total))
    except ValueError:
        pass  # ignore word if its count was not an integer

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
