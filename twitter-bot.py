#!/usr/bin/env python3

# Created on 04/04/2019
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Read reddit posts from JSON and create tweets

import tweepy 
import datetime
import os
import json

today = datetime.datetime.today().strftime('%Y%m%d')
posts_file = "-posts-" + today + ".json"

subreddits_list = ['artificial', 'futurology', 'MachineLearning', 'compsci', 'learnprogramming']

#read in json objects from randomly select reddit json file
#we need to load only if nonempty of course
def read_reddit_posts():
    #

    for subreddit in subreddits_list:
        posts = subreddit + posts_file

        if os.path.getsize(posts) > 0:
            with open(posts, 'r') as f:
                data = json.load(f)

    return data #this works but obviously overwrites each loop...

#create twitter post based on randomly selected reddit post from json objects

#pop the selected post from the objects and rewrite the json file out


def main():
    posts = read_reddit_posts()

    print(posts)

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