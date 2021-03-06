import json
import re
import nltk
from nltk import word_tokenize


#extract tweets
tweets = []
for tweet in open('python.json', 'r'):
    tweets.append(json.loads(tweet)["text"])

#removes https (links, photos)
removedTweets = []
for tweet in tweets:
    tempTweet = re.sub(r"(?:\@|https?\://)\S+", "", tweet)
    tempTweet = re.sub(r'RT @\w+: ', '', tweet)
    removedTweets.append(tempTweet)

#tokenizing text
data = []
for tweet in removedTweets:
    data.append(word_tokenize(tweet))

#test
for i in range (0,10):
    print (removedTweets[i].encode("utf-8"))
    #print(data[i])

features_train, features_test, labels_train, labels_test

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train, labels_train)
