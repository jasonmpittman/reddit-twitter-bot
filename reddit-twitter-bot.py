#!/usr/bin/env python3

# Created on 03/25/2019
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Pull content from specific subreddits and post to Twitter
import config
import praw
import tweepy

#reddit auth


reddit = praw.Reddit(client_id=config.REDDIT_CLIENT_ID, 
    client_secret=config.REDDIT_CLIENT_SECRET, 
    password=config.REDDIT_PASSWORD, 
    user_agent='aggregator bot by /u/drjmp', 
    username=config.REDDIT_USER)

reddit.read_only = True

subreddit = reddit.subreddit('artificial')

for submission in subreddit.hot(limit=5):
    print(submission.title)
    print("\n")
    print(submission.selftext)



# build tweet


# post tweet