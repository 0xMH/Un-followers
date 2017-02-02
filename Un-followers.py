#!python
__author__ ='mhamza'
'''This is a small script I built using tweepy to remove
    all followers That you are not following in twitter
    aka(Block then unblock them).
    You just need to get your keys from apps.twitter.com and entering you @name underneath
    if you have any questions, contact me at M.hamza20@icloud.com.'''
import tweepy
import time
consumer_key = '<consumer_key>'
consumer_secret = '<consumer_secret>'
access_token = '<access_token>'
access_token_secret = '<access_token_secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
Followed = api.friends_ids('your @name')

while True:
    try:
        for user in api.followers_ids():
            #users not in your following List will be blocked then unblocked
            #if you want to remove 'all' your followers u can easly remove the next condition
            if user not in Followed:
                api.create_block(user)
                api.destroy_block(user)
                print('print user %s is removed now'% api.get_user(user).screen_name)

    except tweepy.TweepError as d:
        print(d)
        time.sleep(60*10)
        if user not in Followed:
            api.create_block(user)
            api.destroy_block(user)
            print('print user %s is removed now' % api.get_user(user).screen_name)


    except StopIteration as f:
        print(f)
        break



