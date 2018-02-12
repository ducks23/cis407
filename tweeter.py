# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

from twython import Twython
ACCESS_TOKEN  = "63647409-eP9tp8KKWuWK1thrH4zWQWrzOapij0e4U9mwqDQdC"
ACCESS_SECRET = "lb68nYCgrf43WOHONs5KAOGVuJZKCdVh0uOPwsYQiBpBf"
CONSUMER_KEY = " QiQIve2tcUGxFmR0CIS7Cehsc"
CONSUMER_SECRET =  "vQPInEDRBQOeoxWW7Pl7bhvOKXZSkitzIyGpiuKaIuAdUCrAwp"

twitter = Twython(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter.update_status(status="Hello from Python! :D")
# Variables that contains the user credentials to access Twitter API 

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print(json.dumps(tweet))  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 
