# sentimentlisener.py
"""Script that searches for tweets that match a search string
and tallies the number of positive, neutral and negative tweets."""
import keys
import preprocessor as p 
import sys
from textblob import TextBlob
import tweepy

class SentimentListener(tweepy.StreamListener):
    """Handles incoming Tweet stream."""

    def __init__(self, api, sentiment_dict, topic, limit=10):
        """Configure the SentimentListener."""
        self.sentiment_dict = sentiment_dict
        self.tweet_count = 0
        self.topic = topic
        self.TWEET_LIMIT = limit

        # set tweet-preprocessor to remove URLs/reserved words
        p.set_options(p.OPT.URL, p.OPT.RESERVED) 
        super().__init__(api)  # call superclass's init

    def on_status(self, status):
        """Called when Twitter pushes a new tweet to you."""
        # get the tweet's text
        try:  
            tweet_text = status.extended_tweet.full_text
        except: 
            tweet_text = status.text

        # ignore retweets 
        if tweet_text.startswith('RT'):
            return

        tweet_text = p.clean(tweet_text)  # clean the tweet
        
        # ignore tweet if the topic is not in the tweet text
        if self.topic.lower() not in tweet_text.lower():
            return

        # update self.sentiment_dict with the polarity
        blob = TextBlob(tweet_text)
        if blob.sentiment.polarity > 0:
            sentiment = '+'
            self.sentiment_dict['positive'] += 1 
        elif blob.sentiment.polarity == 0:
            sentiment = ' '
            self.sentiment_dict['neutral'] += 1 
        else:
            sentiment = '-'
            self.sentiment_dict['negative'] += 1 
            
        # display the tweet
        print(f'{sentiment} {status.user.screen_name}: {tweet_text}\n')
        
        self.tweet_count += 1  # track number of tweets processed

        # if TWEET_LIMIT is reached, return False to terminate streaming
        return self.tweet_count < self.TWEET_LIMIT

def main():
    # configure the OAuthHandler
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    # get the API object
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)
                 
    # create the StreamListener subclass object
    search_key = sys.argv[1]
    limit = int(sys.argv[2])  # number of tweets to tally
    sentiment_dict = {'positive': 0, 'neutral': 0, 'negative': 0}
    sentiment_listener = SentimentListener(api, 
        sentiment_dict, search_key, limit)

    # set up Stream 
    stream = tweepy.Stream(auth=api.auth, listener=sentiment_listener)

    # start filtering English tweets containing search_key
    stream.filter(track=[search_key], languages=['en'], is_async=False)  

    print(f'Tweet sentiment for "{search_key}"')
    print('Positive:', sentiment_dict['positive'])
    print(' Neutral:', sentiment_dict['neutral'])
    print('Negative:', sentiment_dict['negative'])

# call main if this file is executed as a script
if __name__ == '__main__':
    main()

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
