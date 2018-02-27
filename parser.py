from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


with open("hockey.json", "r") as n:
	line = n.readline()
	tweet = json.loads(line)
	print(json.dumps(tweet, indent=4))