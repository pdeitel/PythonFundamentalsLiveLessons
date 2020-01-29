# starttweetstream.py
"""Script to get tweets on topic(s) specified as script argument(s) 
   and send tweet text to a socket for processing by Spark."""
import keys
import socket
import sys
import tweepy

class TweetListener(tweepy.StreamListener):
    """Handles incoming Tweet stream."""

    def __init__(self, api, connection, limit=10000):
        """Create instance variables for tracking number of tweets."""
        self.connection = connection
        self.tweet_count = 0
        self.TWEET_LIMIT = limit  # 10,000 by default
        super().__init__(api)  # call superclass's init

    def on_connect(self):
        """Called when your connection attempt is successful, enabling 
        you to perform appropriate application tasks at that point."""
        print('Successfully connected to Twitter\n')

    def on_status(self, status):
        """Called when Twitter pushes a new tweet to you."""
        # get the hashtags
        hashtags = []

        for hashtag_dict in status.entities['hashtags']:
            hashtags.append(hashtag_dict['text'].lower())

        hashtags_string = ' '.join(hashtags) + '\n'
        print(f'Screen name: {status.user.screen_name}:')
        print(f'   Hashtags: {hashtags_string}')
        self.tweet_count += 1  # track number of tweets processed
                
        try:
            # send requires bytes, so encode the string in utf-8 format
            self.connection.send(hashtags_string.encode('utf-8'))  
        except Exception as e:
            print(f'Error: {e}')

        # if TWEET_LIMIT is reached, return False to terminate streaming
        return self.tweet_count != self.TWEET_LIMIT
    
    def on_error(self, status):
        print(status)
        return True
        
if __name__ == '__main__':
    tweet_limit = int(sys.argv[1])  # get maximum number of tweets
    client_socket = socket.socket()  # create a socket 
    
    # app will use localhost (this computer) port 9876
    client_socket.bind(('localhost', 9876))  
 
    print('Waiting for connection')
    client_socket.listen()  # wait for client to connect
    
    # when connection received, get connection/client address
    connection, address = client_socket.accept()  
    print(f'Connection received from {address}')
 
    # configure Twitter access
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    
    # configure Tweepy to wait if Twitter rate limits are reached
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)               
 
    # create the Stream
    twitter_stream = tweepy.Stream(api.auth, 
        TweetListener(api, connection, tweet_limit))

    # sys.argv[2] is the first search term
    twitter_stream.filter(track=sys.argv[2:]) 

    connection.close()
    client_socket.close()

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
