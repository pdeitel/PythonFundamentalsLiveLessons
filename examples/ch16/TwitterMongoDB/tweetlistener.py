# tweetlistener.py
"""TweetListener downloads tweets and stores them in MongoDB."""
import json
import tweepy

class TweetListener(tweepy.StreamListener):
    """Handles incoming Tweet stream."""

    def __init__(self, api, database, limit=10000):
        """Create instance variables for tracking number of tweets."""
        self.db = database
        self.tweet_count = 0
        self.TWEET_LIMIT = limit  # 10,000 by default
        super().__init__(api)  # call superclass's init

    def on_connect(self):
        """Called when your connection attempt is successful, enabling 
        you to perform appropriate application tasks at that point."""
        print('Successfully connected to Twitter\n')

    def on_data(self, data):
        """Called when Twitter pushes a new tweet to you."""
        self.tweet_count += 1  # track number of tweets processed
        json_data = json.loads(data)  # convert string to JSON
        self.db.tweets.insert_one(json_data)  # store in tweets collection
        print(f'    Screen name: {json_data["user"]["name"]}') 
        print(f'     Created at: {json_data["created_at"]}')         
        print(f'Tweets received: {self.tweet_count}')         

        # if TWEET_LIMIT is reached, return False to terminate streaming
        return self.tweet_count != self.TWEET_LIMIT
    
    def on_error(self, status):
        print(f'Error: {status}')
        return True

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
