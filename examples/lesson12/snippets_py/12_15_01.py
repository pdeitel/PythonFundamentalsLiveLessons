# Section 12.15.1 snippets

# Get the API Object
from tweetutilities import get_API

api = get_API()

# Collections Required By LocationListener
tweets = [] 

counts = {'total_tweets': 0, 'locations': 0}

# Creating the LocationListener 
from locationlistener import LocationListener

location_listener = LocationListener(api, counts_dict=counts, 
    tweets_list=tweets, topic='football', limit=50)  

# Configure and Start the Stream of Tweets
import tweepy

stream = tweepy.Stream(auth=api.auth, listener=location_listener)

stream.filter(track=['football'], languages=['en'], is_async=False)

# Displaying the Location Statistics
counts['total_tweets']

counts['locations']

print(f'{counts["locations"] / counts["total_tweets"]:.1%}')

# Geocoding the Locations
from tweetutilities import get_geocodes

bad_locations = get_geocodes(tweets)

# Displaying the Bad Location Statistics
bad_locations

print(f'{bad_locations / counts["locations"]:.1%}')

# Cleaning the Data
import pandas as pd

df = pd.DataFrame(tweets)

df = df.dropna()

# Creating a Map with Folium
import folium

usmap = folium.Map(location=[39.8283, -98.5795], tiles='Stamen Terrain',
                   zoom_start=5, detect_retina=True)

# Creating Popup Markers for the Tweet Locations
for t in df.itertuples():
     text = ': '.join([t.screen_name, t.text])
     popup = folium.Popup(text, parse_html=True)
     marker = folium.Marker((t.latitude, t.longitude), 
                            popup=popup)
     marker.add_to(usmap)

# Saving the Map
usmap.save('tweet_map.html')




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
