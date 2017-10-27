import tweepy

from secrets import *



auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(Access_Token, Access_Token_Secret)

api = tweepy.API(auth)

# download home limeline tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)