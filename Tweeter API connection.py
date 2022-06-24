#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import tweepy as tw
import pandas as pd


# In[2]:


consumer_key= 'wQm9UJP2FpxQBqOmBBIPjCP0X'
consumer_secret= '2PDEIoZ3qIA2sYZyG2g5XHiLvOQbxRKpMbmJixGmXdrL1W8Ju0'
access_token= '1171806772111269888-yoScVhhG18tUVcYWH8PkuMKtJxGsuj'
access_token_secret= 'kj04cXv5AVsyRisKvGfV740QK6jlLzAMkHkWSWGpJWiTv'


# In[3]:


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# In[4]:


search_words = "#covid19"
date_since = "2022-03-24"


# In[5]:


tweets = tw.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since=date_since).items(5000)
tweets


# In[7]:


tweets = tw.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since=date_since).items(100)
tweets


# In[8]:


[tweet.text for tweet in tweets]


# In[9]:


new_search = search_words + " -filter:retweets"
new_search

tweets = tw.Cursor(api.search_tweets,
              q=new_search,
              lang="en",
              since=date_since).items(100)
tweets

[tweet.text for tweet in tweets]


# In[ ]:




