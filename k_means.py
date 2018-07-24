import json
import re
import nltk
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer


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
#for tweet in removedTweets:
#    data.append(word_tokenize(tweet))

#vectorized data
vectorizer = CountVectorizer(min_df=1)
data = vectorizer.fit_transform([tweet])


from sklearn.cluster import KMeans
import numpy as np


#smaller_data = data[:len(data)/100] 
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print