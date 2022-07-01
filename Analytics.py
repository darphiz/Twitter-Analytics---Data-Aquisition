import tweepy
import json

API_KEY = "" 
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = "" 

#Authenticate
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_words = "startup tips -filter:retweets -filter:links"
last_id = 1512015569649868806


tweets = tweepy.Cursor(api.search_tweets,        
        q = search_words,
        result_type = "mixed",
        tweet_mode = "extended",
        lang = "en",
        count = 100,
        max_id = last_id -1
        ).items(1000)

#convert tweets to python dictionary
print("Converting Tweets to JSON")
tweets_data = [tweet._json for tweet in tweets]
print("Conversion Complete")
with open('tweets.json', 'w') as f:
    json.dump(tweets_data, f)
print("Tweets saved to file")