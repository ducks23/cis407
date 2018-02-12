from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


with open('f.json', 'r') as n:
	distros_dict = json.load(n)

for distro in range(0,100):
	print(distros_dict[distro])