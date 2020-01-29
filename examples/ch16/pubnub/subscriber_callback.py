# subscriber_callback.py
"""PubNub SubscribeCallback subclass that processes stock orders
   and places the new prices in a pandas DataFrame."""
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory

class SensorSubscriberCallback(SubscribeCallback):
    """SensorSubscriberCallback receives messages from PubNub."""
    def __init__(self, df, companies, anim, limit=1000):
        """Create instance variables for tracking number of tweets."""
        self.df = df  # DataFrame in which to store prices
        self.symbols = companies  # for updating correct DataFrame row
        self.anim = anim  # animation to stop when limit is reached  
        self.order_count = 0
        self.MAX_ORDERS = limit  # 1000 by default
        super().__init__()  # call superclass's init

    def status(self, pubnub, status):
        print('status:', status)
        if status.category == PNStatusCategory.PNConnectedCategory:
            print('Connected to PubNub')
        elif status.category == PNStatusCategory.PNDisconnectedCategory:
            print('Disconnected from PubNub')
 
    def message(self, pubnub, message):
        symbol = message.message['symbol']  # extract company name
        bid_price = message.message['bid_price']  # extract prices
        self.df.at[self.symbols.index(symbol), 'price'] = bid_price
        self.order_count += 1
        
        # if MAX_ORDERS is reached, unsubscribe from PubNub channel
        if self.order_count == self.MAX_ORDERS:
            print('Max orders processed. Unsibscribing.')
            pubnub.unsubscribe_all()
            self.anim.event_source().stop()
            

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