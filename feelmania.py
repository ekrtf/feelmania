import tweepy
from textblob import TextBlob

consumer_key = "<insert key here>"
consumer_secret = "<insert secret here>"

access_token = "<insert token here>"
access_token_secret = "<insert token secret here>"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_tokem, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Flower')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment.polarity)