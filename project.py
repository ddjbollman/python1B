import tweepy
from time import sleep
from secrets import *



auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(Access_Token, Access_Token_Secret)

api = tweepy.API(auth)

# download home limeline tweets
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

# open file under default read mode
my_file = open('20ksea.txt', 'r')

# read each line and save it to a variable
file_lines = my_file.readlines()

# close file, good behavior.
my_file.close()


for line in file_lines:
    try:
        if line != '\n':
            api.update_status(line)
            #print(line)
            sleep(900)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(2)




file_lines.