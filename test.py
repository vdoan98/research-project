import json
import re
import nltk
from nltk import word_tokenize

tweet = "RT @TheBrandonMorse: Believe me. Too many men are too feminine. \n\nWe desperately need a return to masculinity. https:\/\/t.co\/w4MFW6zAdu"

#removes https (links, photos)
tempTweet = re.sub(r"http\S+", "", tweet)
tempTweet = re.sub(r'RT @\w+: ', '', tempTweet)

print(tempTweet)

