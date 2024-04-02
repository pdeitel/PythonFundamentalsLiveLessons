# stocklistener.py
"""Visualizing a PubNub live stream."""
from matplotlib import animation
import matplotlib.pyplot as plt
import pandas as pd
import random 
import seaborn as sns
import sys

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

companies = ['Apple', 'Bespin Gas', 'Elerium', 'Google', 'Linen Cloth']

# DataFrame to store last stock prices 
companies_df = pd.DataFrame(
    {'company': companies, 'price' : [0, 0, 0, 0, 0]})
 
class SensorSubscriberCallback(SubscribeCallback):
    """SensorSubscriberCallback receives messages from PubNub."""
    def __init__(self, df, limit=1000):
        """Create instance variables for tracking number of tweets."""
        self.df = df  # DataFrame to store last stock prices
        self.order_count = 0
        self.MAX_ORDERS = limit  # 1000 by default
        super().__init__()  # call superclass's init

    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNConnectedCategory:
            print('Subscribed')
        elif status.category == PNStatusCategory.PNAcknowledgmentCategory:
            print('Unsubscribed')
 
    def message(self, pubnub, message):
        symbol = message.message['symbol']
        bid_price = message.message['bid_price']
        print(symbol, bid_price)
        self.df.at[companies.index(symbol), 'price'] = bid_price
        self.order_count += 1
        
        # if MAX_ORDERS is reached, unsubscribe from PubNub channel
        if self.order_count == self.MAX_ORDERS:
            pubnub.unsubscribe_all()
            
def update(frame_number):
    """Configures bar plot contents for each animation frame."""
    plt.cla()  # clear old barplot
    axes = sns.barplot(
        data=companies_df, x='company', y='price', palette='cool') 
    axes.set(xlabel='Company', ylabel='Price')  
    plt.tight_layout()

if __name__ == '__main__':
    sns.set_style('whitegrid')  # white background with gray grid lines
    figure = plt.figure('Stock Prices')  # Figure for animation

    # configure and start animation that calls function update
    stock_animation = animation.FuncAnimation(
        figure, update, repeat=False, interval=33)
    plt.show(block=False)  # display window

    # set up pubnub-market-orders sensor stream key
    config = PNConfiguration()
    config.subscribe_key = 'YOUR KEY HERE'
 
    # create PubNub client and register a SubscribeCallback
    pubnub = PubNub(config) 
    pubnub.add_listener(
        SensorSubscriberCallback(df=companies_df, 
            limit=int(sys.argv[1] if len(sys.argv) > 1 else 1000))
        
    # subscribe to pubnub-sensor-network channel and begin streaming
    pubnub.subscribe().channels('pubnub-market-orders').execute()
    
    plt.show()  # keeps graph on screen until you dismiss its window

#**************************************************************************
#* (C) Copyright 1992-2018 by Deitel & Associates, Inc. and               *
#* Pearson Education, Inc. All Rights Reserved.                           *
#*                                                                        *
#* DISCLAIMER: The authors and publisher of this book have used their     *
#* best efforts in preparing the book. These efforts include the          *
#* development, research, and testing of the theories and programs        *
#* to determine their effectiveness. The authors and publisher make       *
#* no warranty of any kind, expressed or implied, with regard to these    *
#* programs or to the documentation contained in these books. The authors *
#* and publisher shall not be liable in any event for incidental or       *
#* consequential damages in connection with, or arising out of, the       *
#* furnishing, performance, or use of these programs.                     *
#**************************************************************************    
    
    

