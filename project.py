import tweepy

ConsumerKey = 'a6yPaALlcpQbp46mmxuu7L9dC'
ConsumerSecret = '6AqSkoyu6GOn5azWu9Rs4rtRxFbSXpt3Z12rzDdzqnXPLSKSW1'
Access_Token = '802997337563873280-aTBPaWhdseyzAUqYgT3oRLTX5Cp49i7'
Access_Token_Secret	= 'tsQwesezzRtdpudqXIlEc4gFpCu6gjARF3V3Kmn25MH2J'

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text