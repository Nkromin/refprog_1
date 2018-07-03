import logging
import time
import csv
import json
import pandas
import sys
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from datetime import datetime
from dateutil import parser


# enable logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# authorize the app to access Twitter on our behalf
consumer_key = 'kxlyrSPGz6E3mDoVo2G4TbCzf'
consumer_secret = '3OmApP221fRRCcU66jJayGwwFXMz4DdoFyNPPCd6jNx0nI4FQF'
access_token = '987065552517517312-nwdv2XraOXI0TTjAwX2te0mriO1V6bT'
access_secret = 'CM6Hank7UkPpl7EF03elBM7Ha1flD2KfycDdwn5s5Oo1s'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# establish open connection to streaming API
class MyListener(StreamListener):
    tweet_number = 0
    def __init__(self, max_tweet):
        self.max_tweet=max_tweet

    def on_data(self, data):
        try:
            self.tweet_number+=1
            tweet = parse_tweet(data)
            content = extract_content(tweet)
            with open('RahulStream.csv', 'a') as f:
                writer = csv.writer(f, quotechar = '"')
                writer.writerow(content)
                #logger.info(content[3])

        except BaseException as e:
            logger.warning(e)

        if self.tweet_number>=self.max_tweet:
            sys.exit()
        else:
            return True

    def on_error(self, status):
        logger.warning(status)
        return True


# parse data
def parse_tweet(data):

    # load JSON item into a dict
    tweet = json.loads(data)


    # check if tweet is valid
    if('user' in tweet.keys() and tweet['user']['lang']=="en"):

        # parse date
        tweet['CREATED_AT'] = parser.parse(tweet['created_at'])

        # classify tweet type based on metadata
        if 'retweeted_status' in tweet:
            tweet['TWEET_TYPE'] = 'retweet'

        elif len(tweet['entities']['user_mentions']) > 0:
            tweet['TWEET_TYPE'] = 'mention'

        else:
            tweet['TWEET_TYPE'] = 'tweet'

        return tweet

    else:
        logger.warning("Imcomplete tweet: %s", tweet)


# extract relevant data to write to CSV
def extract_content(tweet):

    content = [tweet['user']['screen_name'],
               tweet['CREATED_AT'].strftime('%Y-%m-%d %H:%M:%S'),
               tweet['text'].encode('unicode_escape')]

    return content


def restart_stream(val):

    while True:

        logger.warning("Twitter API Connection opened")

        try:
            twitter_stream = Stream(auth,MyListener(max_tweet=3500))
            twitter_stream.filter(track=['rahulgandhi'])

        except Exception as e:
            logger.warning(e)
            continue

        finally:
            logger.warning("Twitter API Connection closed")


if __name__ == '__main__':
    val=11
    restart_stream(val)
    print("\n ********\n*****\n***\n*****Script Completed******************")




'''


import logging
import time
import csv
import json
import sys
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from datetime import datetime
from dateutil import parser
from time import sleep
from threading import Thread
i=0
politician=""

# enable logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# authorize the app to access Twitter on our behalf
consumer_key = 'kxlyrSPGz6E3mDoVo2G4TbCzf'
consumer_secret = '3OmApP221fRRCcU66jJayGwwFXMz4DdoFyNPPCd6jNx0nI4FQF'
access_token = '987065552517517312-nwdv2XraOXI0TTjAwX2te0mriO1V6bT'
access_secret = 'CM6Hank7UkPpl7EF03elBM7Ha1flD2KfycDdwn5s5Oo1s'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# establish open connection to streaming API
class MyListener(StreamListener):
    tweet_number = 0
    def __init__(self, max_tweet):
        self.max_tweet=max_tweet

    def on_data(self, data):
        self.tweet_number+=1
        try:

            tweet = parse_tweet(data)
            content = extract_content(tweet)
            with open(politician+".csv", 'a') as f:
                print(politician)
                writer = csv.writer(f, quotechar = '"')
                writer.writerow(content)


        except BaseException as e:
            logger.warning(e)
            return False

        if self.tweet_number>=self.max_tweet:
            sys.exit()
        else:
            return True

    def on_error(self, status):
        logger.warning(status)
        return False


# parse data
def parse_tweet(data):

    # load JSON item into a dict
    tweet = json.loads(data)


    # check if tweet is valid
    if 'user' in tweet.keys():

        # parse date
        tweet['CREATED_AT'] = parser.parse(tweet['created_at'])

        # classify tweet type based on metadata
        if 'retweeted_status' in tweet:
            tweet['TWEET_TYPE'] = 'retweet'

        elif len(tweet['entities']['user_mentions']) > 0:
            tweet['TWEET_TYPE'] = 'mention'

        else:
            tweet['TWEET_TYPE'] = 'tweet'

        return tweet

    else:
        logger.warning("Imcomplete tweet: %s", tweet)


# extract relevant data to write to CSV
def extract_content(tweet):

    content = [tweet['user']['screen_name'],
               tweet['CREATED_AT'].strftime('%Y-%m-%d %H:%M:%S'),
               tweet['text'].encode("utf-8")]

    return content


def start_stream(politician):
    while(True):
        logger.warning("Twitter API Connection opened")
        try:

            twitter_stream = Stream(auth, MyListener(max_tweet=20))
            twitter_stream.filter(track=[politician])

        except Exception as e:
            logger.warning(e)
            continue

        finally:
            logger.warning("Twitter API Connection closed")



if __name__ == '__main__':
    politician="narendramodi"
    start_stream(politician)







 '''
