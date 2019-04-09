#!/usr/bin/env python3

# Created on 03/25/2019
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Pull content from specific subreddits and serialize to JSON
import config
import praw
import datetime
import json

today = datetime.datetime.today().strftime('%Y%m%d')

posts_file = "-posts-" + today + ".json"

# to add a new subreddit, add the name to this array and the tags to the dictoinary below using name: tags format
subreddits_list = ['artificial', 'futurology', 'MachineLearning', 'compsci', 'learnprogramming']

tags = {
        "artificial": "#AI #ArtificialIntelligence #drjmpBot",
        "futurology": '#futurology #drjmpBot',
        "MachineLearning": '#MachineLearning, #drjmpBot', 
        "compsci": '#ComputerScience #drjmpbot',
        "learnprogramming": '#learnprogramming, #drjmpbot'
}

#the subreddit pull in PRAW gets the home banner. we want to strip them
blacklist_posts = {
        "artificial": "Welcome to /r/artificial!",
        "futurology": "r/Futurology's Official Discord",
        "MachineLearning": "[N] Chat with us on Slack!",
        "compsci": "CompSci Weekend SuperThread",
        "learnprogramming": "New? READ ME FIRST!"
}

# write out the daily list of reddit posts we want to use for twitter
def write_reddit_list(posts, subreddit):

    data = {}
    data['posts'] = []
    
    # do in loop
    for post in posts:
        if blacklist_posts[subreddit] not in post.title:
            data['posts'].append( {
                'title': post.title,
                'url': post.url,
                'tags': tags[subreddit]
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