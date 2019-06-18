# locationlistener.py
"""Receives tweets matching a search string and stores a list of
dictionaries containing each tweet's screen_name/text/location."""
import tweepy
from tweetutilities import get_tweet_content

class LocationListener(tweepy.StreamListener):
    """Handles incoming Tweet stream to get location data."""

    def __init__(self, api, counts_dict, tweets_list, topic, limit=10):
        """Configure the LocationListener."""
        self.tweets_list = tweets_list
        self.counts_dict = counts_dict
        self.topic = topic
        self.TWEET_LIMIT = limit
        super().__init__(api)  # call superclass's init

    def on_status(self, status):
        """Called when Twitter pushes a new tweet to you."""
        # get each tweet's screen_name, text and location
        tweet_data = get_tweet_content(status, location=True)  

        # ignore retweets and tweets that do not contain the topic
        if (tweet_data['text'].startswith('RT') or
            self.topic.lower() not in tweet_data['text'].lower()):
            return

        self.counts_dict['total_tweets'] += 1  # original tweet

        # ignore tweets with no location 
        if not status.user.location:  
            return

        self.counts_dict['locations'] += 1  # tweet with location
        self.tweets_list.append(tweet_data)  # store the tweet
        print(f'{status.user.screen_name}: {tweet_data["text"]}\n')

        # if TWEET_LIMIT is reached, return False to terminate streaming
        return self.counts_dict['locations'] < self.TWEET_LIMIT



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
