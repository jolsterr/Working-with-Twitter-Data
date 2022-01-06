# Importing the libraries
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
# from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import contentanalysis
# Authentications 
auth = tweepy.OAuthHandler(contentanalysis.CONSUMER_KEY, contentanalysis.CONSUMER_SECRET)
auth.set_access_token(contentanalysis.ACCESS_TOKEN, contentanalysis.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
client = tweepy.Client(contentanalysis.BEARER_TOKEN)
query = 'sustainable lang:en'
file_name = 'tweets.txt'

# Transferring the Tweets into the Tweets.txt files
with open(file_name, 'a+') as filehandler:
    response = client.search_recent_tweets(query=query, max_results=30, user_fields = ['username', 'location'], tweet_fields = ['created_at'], expansions=['author_id'])
    filehandler.write('{0}\n'.format(response))
    # print(response)

users = {u['id']: u for u in response.includes['users']}
columns = ['Time', 'User', 'Tweet']
data = []
max_results = 30
tweets =[]
time = []

for i in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=30, user_fields = ['username', 'location'], tweet_fields = ['created_at'], expansions=['author_id']).flatten(limit=50):
    data.append([i.created_at, i.author_id, i.text])

df = pd.DataFrame(data, columns=columns)
df.to_csv('tweetsdetailed.csv')

