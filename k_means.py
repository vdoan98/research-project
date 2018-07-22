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
    data.append(word_tokenzie(tweet))


#Graphing data
def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()


#Features of data
feature_1 = 'liberal'
feature_2 = 'conservative'
features_list = [feature_1, feature_2]
data = featureFormat()

from sklearn.cluster import KMeans
import numpy as np

kmeans = KMeans(n_clusters=2)
kmeans.fit()
