#!/usr/bin/env python3

# Created on 04/04/2019
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Read reddit posts from JSON and create tweets

import tweepy 
import datetime
import os
import json
import sys
import config

today = datetime.datetime.today().strftime('%Y%m%d')
posts_file = "-posts-" + today + ".json"

subreddits_list = ['artificial', 'futurology', 'MachineLearning', 'compsci', 'learnprogramming']

def read_reddit_posts(subreddit): 
    data = {}

    posts = subreddit + posts_file

    if os.path.getsize(posts) > 0:
        with open(posts, 'r') as json_file:
            data = json.load(json_file) 

    try:
        post = data['posts'][0]
    except IndexError:
        #call reddit bot with specific subreddit parameter
        read_reddit_posts(subreddit)

    try:
        del data['posts'][0]
    except IndexError:
        print("There was an index out of bounds during the del function")
    
    with open(posts, 'w') as json_file:
        json.dump(data, json_file)

    return post



def post_tweet(post):
    auth = tweepy.OAuthHandler(config.TWITTER_API_KEY, config.TWITTER_API_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # build and post tweet
    tweet = post['title'] + "\n" + post['url'] + "\n" + post['tags']
    print(tweet)
    #api.update_status(tweet) 

def main():
    subreddit = sys.argv[1]
    post = read_reddit_posts(subreddit)
    post_tweet(post)  
    
main()