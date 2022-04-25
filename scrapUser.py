import tweepy
import time
import pandas as pd
import streamlit as st
import path as p

# st.cache(suppress_st_warning=False)
def scrapUser(username,count,api):

      count = min(100,count)

      dilog = st.text(f'Scrapping Tweets for {username}')

      # Creation of query method using parameters
      tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
      print(tweets)
      # Pulling information from tweets iterable object
      tweets_list = [[tweet.text, tweet.created_at, tweet.id_str, tweet.user.name, tweet.user.id_str, tweet.user.location, tweet.user.description, tweet.user.verified, tweet.user.followers_count, tweet.user.created_at] for tweet in tweets]
      
      # Creation of dataframe from tweets list
      # Add or remove columns as you remove tweet information
      tweets_df = pd.DataFrame(tweets_list,columns=['text','created_at','tweet_id','username','user_id','location','description','verified','followers','acc_cre_date'])
      # print(tweets_df.columns,tweets_df.head(3))

      tweets_df['chk'] =str(username)+str(count)

      filename = p.path2

    #  tweets_df.to_csv(filename)
      
      dilog.empty()
      
      print('Scraping For User has completed!')
      return tweets_df

def start(username,count):
    consumer_key = '2nfUSbc9DwMjZ46x6QpiirZ4y'
    consumer_secret = 'jWCFVENF8k5TSP7wAKv7AYnGnGUZKwO4EWRX8FvnoXyzhmgMGu'
    access_key = '2572669031-VBa6Zl6TIW3AEgSvwnX6VsOP6cbwOvB4JmWnQVb'
    access_secret = 'HplKckRXHEyQuwQdJhBTf0SGnux94utNsFEqCyYvBQZy1'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    # api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    api = tweepy.API(auth)
      
    # print("Enter Twitter HashTag to search for")
    # tag = input()
    # print("Enter Date since The Tweets are required in yyyy-mm--dd")
    # date_since = input()
    # numtweet = 10

    return scrapUser(username,count,api)

# scrapUser('OKhilari',2)
