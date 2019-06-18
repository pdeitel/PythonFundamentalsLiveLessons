# 12.13.2 snippets
# Authenticating
import tweepy

import keys

auth = tweepy.OAuthHandler(keys.consumer_key, 
                           keys.consumer_secret)               

auth.set_access_token(keys.access_token, 
                      keys.access_token_secret)
                 
api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)               

# Creating a TweetListener 
from tweetlistener import TweetListener

tweet_listener = TweetListener(api)

# Creating a Stream 
tweet_stream = tweepy.Stream(auth=api.auth, 
                             listener=tweet_listener)
                 
# Starting the TweetListeneret Stream
tweet_stream.filter(track=['Mars Rover'], is_async=True) 

# Asynchronous vs. Synchronous Streams

# Other filter Method Parameters

# Twitter Restrictions Note

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
