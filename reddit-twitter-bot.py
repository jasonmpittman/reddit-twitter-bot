#!/usr/bin/env python3

# Created on 03/25/2019
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Pull content from specific subreddits and post to Twitter
import config
import praw
import tweepy
import time
import json

posts_file = "reddit-posts.json"


# write out the daily list of reddit posts we want to use for twitter
def write_reddit_list(posts):
    
    data = {}
    data['posts'] = []
    
    # do in loop
    for post in posts:
        if post.title != 'Welcome to /r/artificial!':
            data['posts'].append( {
                'title': post.title,
                'url': post.url,
                'tags': "#AI #ArtificialIntelligence #drjmpBot"
            })

    with open(posts_file, 'w') as outfile:
        json.dump(data, outfile)
        

def read_reddit_list(posts_file):
    with open(POSTS, 'r', enconding='utf-8') as f:
        posts = f.readlines()
    
    return posts


#reddit
reddit = praw.Reddit(client_id=config.REDDIT_CLIENT_ID, 
    client_secret=config.REDDIT_CLIENT_SECRET, 
    password=config.REDDIT_PASSWORD, 
    user_agent='aggregator bot by /u/drjmp', 
    username=config.REDDIT_USER)

reddit.read_only = True

subreddit = reddit.subreddit('artificial')

write_reddit_list(subreddit.hot(limit=5))

#twitter
auth = tweepy.OAuthHandler(config.TWITTER_API_KEY, config.TWITTER_API_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# build and post tweet
#for submission in subreddit.hot(limit=3):
#    if submission.title != 'Welcome to /r/artificial!':
#        tweet = submission.title + "\n" + submission.url + "\n" "#AI #ArtificialIntelligence #drjmpBot"
#        api.update_status(tweet) 
#        time.sleep(5)