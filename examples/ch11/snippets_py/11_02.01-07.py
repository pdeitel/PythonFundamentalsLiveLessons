# Section 11.2.1 snippets
from textblob import TextBlob

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

blob = TextBlob(text)

blob


# Section 11.2.2 snippets
blob.sentences

blob.words


# Section 11.2.3 snippets
blob

blob.tags


# Section 11.2.4 snippets
blob

blob.noun_phrases


# Section 11.2.5 snippets

# Getting the Sentiment of a TextBlob
blob

blob.sentiment

# Getting the polarity and subjectivity from the Sentiment Object
%precision 3

blob.sentiment.polarity

blob.sentiment.subjectivity

# Getting the Sentiment of a Sentence 
for sentence in blob.sentences:
    print(sentence.sentiment)


# Section 11.2.6 snippets
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

blob

blob.sentiment

for sentence in blob.sentences:
    print(sentence.sentiment)
    

# Section 11.2.7 snippets
blob

blob.detect_language()

spanish = blob.translate(to='es')

spanish

spanish.detect_language()

chinese = blob.translate(to='zh')

chinese

chinese.detect_language()

spanish.translate()

chinese.translate() 



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
