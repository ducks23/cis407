from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
#this is my project for the class

access_token = "63647409-aGEHHskJhluZFSuR7zV1PgUDRrWJTEjYj9YE82SaV"
access_token_secret = "kjx8ets5psdZwgHnJy7gqZccnbkCDbiqeggFUaoSQWP9A"
consumer_key = "HGsZXt7tWobrtdS6NhAtl0m1E"
consumer_secret =  "OHnLgBJmQsJhBMafGiwPeKCRAm1DknXjpzRM7GYccWFTVGny3r"
class StdOutListener(StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        file = open('f.json', 'w')
        json.dump(decoded, file, sort_keys = True, indent = 4)
        print("writing tweet ctrl + c to quit")
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=["spacex", "elon musk", "university of oregon"])

