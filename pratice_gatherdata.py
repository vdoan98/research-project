import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = 'z7d23cQWW3IE9IMFOV5DwjDzm'
consumer_secret = 'COUn7QLcCDUj8ct8DLxY9kEjcfkOC3FNqXEr9q0x8hmOhyZrJE'

access_token = '941707847238373376-R4517e2MlbF1T3kGSOnRJmA2ay0MGZy'
access_token_secret = 'wBQklX4XgWaLGXRw7kWW9mxSpAA4wyQF1VIdHnXzP94WF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True 
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    
    def on_error(self, status):
        print(status)
        return True

    

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#prolife', '#prochoice', '#antilife', '#antichoice'])