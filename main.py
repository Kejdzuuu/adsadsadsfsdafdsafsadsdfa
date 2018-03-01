import tweepy as tp
import time
import os
import requests

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

cant_destroy = True
while(cant_destroy):
    try:
        test = api.favorites()
        cant_destroy = False
    except:
        print('nej, will try again in 100 seconds')
        time.sleep(100)

length = len(test)
while(length is not 0):
    try:
        length = len(test)
        for t in test:
            api.destroy_favorite(t.id)
        print('unfavourited ' + str(length) + ' tweets')
        test = api.favorites()
    except:
        print('nej, will try again in 100 seconds')
        time.sleep(100)
        length = 1




print('fin')