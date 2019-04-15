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

today = datetime.datetime.today().strftime('%Y%m%d')
posts_file = "-posts-" + today + ".json"

subreddits_list = ['artificial', 'futurology', 'MachineLearning', 'compsci', 'learnprogramming']

def read_reddit_posts(subreddit): 
    data = {}

    posts = subreddit + posts_file

    if os.path.getsize(posts) > 0:
        with open(posts, 'r') as json_file:
            data = json.load(json_file) 

    post = data['posts'][0]

    #return data #this works
    return post #this correctly selects first post from posts in json

#pop the selected post from the objects and rewrite the json file out


def main():
    subreddit = sys.argv[1]
    post = read_reddit_posts(subreddit)
    print(post)
    #for post in posts['posts']:
        #print(post['title'])
        #print(post['url'])
        #print(post['tags'])
        
    
    

main()

# THIS IS GOING TO MOVE TO ANOTHER SERVICE
#twitter
#auth = tweepy.OAuthHandler(config.TWITTER_API_KEY, config.TWITTER_API_SECRET)
#auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
#api = tweepy.API(auth)

# build and post tweet
#for submission in subreddit.hot(limit=3):
#    if submission.title != 'Welcome to /r/artificial!':
#        tweet = submission.title + "\n" + submission.url + "\n" "#AI #ArtificialIntelligence #drjmpBot"
#        api.update_status(tweet) 
#        time.sleep(5)