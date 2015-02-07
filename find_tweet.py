import re
import twitter
import random
import os
from htmlentitydefs import name2codepoint as n2c

twitter_users = open('twitter_users.txt', 'r').read().splitlines()

def connect():
    api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                          consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                          access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                          access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    return api

# https://github.com/tommeagher/heroku_ebooks/blob/master/ebooks.py
def entity(text):
    if text[:2] == "&#":
        try:
            if text[:3] == "&#x":
                return unichr(int(text[3:-1], 16))
            else:
                return unichr(int(text[2:-1]))
        except ValueError:
            pass
    else:
        guess = text[1:-1]
        numero = n2c[guess]
        try:
            text = unichr(numero)
        except KeyError:
            pass    
    return text

# https://github.com/tommeagher/heroku_ebooks/blob/master/ebooks.py
def filter_tweet(tweet):
    tweet.text = re.sub(r'\b(RT|MT) .+','',tweet.text) #take out anything after RT or MT
    tweet.text = re.sub(r'(\#|@|(h\/t)|(http))\S+','',tweet.text) #Take out URLs, hashtags, hts, etc.
    tweet.text = re.sub(r'\n','', tweet.text) #take out new lines.
    tweet.text = re.sub(r'\"|\(|\)', '', tweet.text) #take out quotes.
    htmlsents = re.findall(r'&\w+;', tweet.text)
    if len(htmlsents) > 0 :
        for item in htmlsents:
            tweet.text = re.sub(item, entity(item), tweet.text)    
    tweet.text = re.sub(r'\xe9', 'e', tweet.text) #take out accented e
    return tweet.text

def grab_tweets(api, user):
    result_tweets=[]
    user_tweets = api.GetUserTimeline(screen_name=user, count=200, max_id=None, include_rts=True, trim_user=True, exclude_replies=True)
    for tweet in user_tweets:
        tweet.text = filter_tweet(tweet)
        if len(tweet.text) != 0:
            result_tweets.append(tweet.text)
    return result_tweets

def get_tweet():
	api = connect()
	user = random.choice(twitter_users)
	tweets = grab_tweets(api, user)
	return random.choice(tweets)
