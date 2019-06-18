# Section 10.4.1 snippets

from timewithproperties import Time

# Creating a `Time` Object
wake_up = Time(hour=6, minute=30)

# Displaying a `Time` Object
wake_up

print(wake_up)

# Getting an Attribute Via a Property 
wake_up.hour

# Setting the `Time` 
wake_up.set_time(hour=7, minute=45)

wake_up

# Setting an Attribute via a Property 
wake_up.hour = 6

wake_up

# Attempting to Set an Invalid Value 
wake_up.hour = 100



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
