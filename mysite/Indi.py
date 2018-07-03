import tweepy
import json
import pandas as pd
from datetime import datetime
#import string as str
import os
# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''
path=""


# Function to extract tweets
def get_tweets(username):

        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)

        # Calling api
        api = tweepy.API(auth)

        # 200 tweets to be extracted
        tweets = api.user_timeline(screen_name=username,count=200)

        # Empty Array
        tmp=[]

        # create array of tweet information: username,
        # tweet id, date/time, text
        tweets_for_csv = [json.loads(json.dumps(tweet._json)) for tweet in tweets] # CSV file created

        for i in tweets_for_csv:
            #print(i.keys())
            if(i["user"]["lang"]=="en"):
                tmp.append([str(i["created_at"]),str(i["text"].encode('unicode_escape')),str(i["retweet_count"]),str(i["favorite_count"])])
                #tmp.append([str(i["text"])])

            else:
                pass
        labels="Date Tweet Retweets Favorite".split()
        #labels="Tweet".split()

        df = pd.DataFrame.from_records(tmp, columns=labels)
        df.to_csv(os.path.join(path,username))

def callout(val):
        get_tweets("narendramodi")
        get_tweets("rahulgandhi")


# Driver code
if __name__ == '__main__':

    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("narendramodi")
    get_tweets("rahulgandhi")
    print("\n ********\n*****\n***\n*****Script Completed******************")



'''



'''
