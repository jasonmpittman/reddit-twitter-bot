#!/usr/bin/env python3

# Created on 03/25/2019
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Pull content from specific subreddits and post to Twitter
import config
import praw
import tweepy
import datetime
import json

today = datetime.datetime.today().strftime('%Y%m%d%H%M%S')

posts_file = "-posts-" + today + ".json"

subreddits_list = ['artificial', 'futurology', 'MachineLearning', 'compsci', 'learnprogramming']

tags = ['#AI #ArtificialIntelligence #drjmpBot', '#futurolog #drjmpBot', '#MachineLearning, #drjmpBot', 
'#ComputerScience #drjmpbot, #learnprogramming, #drjmpbot']

blacklist_posts = ["Welcome to /r/artificial!", ]

# write out the daily list of reddit posts we want to use for twitter
def write_reddit_list(posts, subreddit):
    data = {}
    data['posts'] = []
    
    # do in loop
    for post in posts:
        if post.title != 'Welcome to r/':
            data['posts'].append( {
                'title': post.title,
                'url': post.url,
                #'tags': "#AI #ArtificialIntelligence #drjmpBot"
            })

    with open(subreddit + posts_file, 'a+') as outfile:
        json.dump(data, outfile)
        
def get_reddit_posts():
    reddit = praw.Reddit(client_id=config.REDDIT_CLIENT_ID, 
    client_secret=config.REDDIT_CLIENT_SECRET, 
    password=config.REDDIT_PASSWORD, 
    user_agent='aggregator bot by /u/drjmp', 
    username=config.REDDIT_USER)

    reddit.read_only = True

    for subreddit in subreddits_list:
        posts = reddit.subreddit(subreddit)
        write_reddit_list(posts.hot(limit=5), subreddit)

def main():
    get_reddit_posts()


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