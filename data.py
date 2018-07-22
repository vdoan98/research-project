import json
import re
from nltk.tokenize import word_tokenize

#extract tweets
tweets = []
for tweet in open('python.json', 'r'):
    tweets.append(json.loads(tweet)["text"])

#removes https (links, photos)
removedTweets = []
for tweet in tweets:
    tempTweet = re.sub(r'http\S+', '', tweet)
    tempTweet = re.sub(r'RT @\w+: ', '', tweet)
    removedTweets.append(tempTweet)

#tokenizing text
data = []
for tweet in removedTweets:
    data.append(word_tokenize(tweet))

#test
for i in range (0,10):
    print (data[i].encode("utf-8"))