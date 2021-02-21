import praw
import json
import re
import datetime

class scraper:
    
    def __init__(self):
        self.id = "AtCPNKHE1zBWeQ"
        self.secret = "qz2Dh8mLFkWlbtIF5ExkNPgvD1ocqA"
        self.username = "TestAcc2682"
        self.agent = "Reddit Searcher"
        self.pw = "testacc"
        self.reddit = praw.Reddit(
            client_id=self.id,
            client_secret=self.secret,
            password=self.pw,
            user_agent = self.agent,
            username=self.username)
    
    def search(self,subreddit,target, lim):
        res = ""
        self.subreddit = self.reddit.subreddit(subreddit)
        self.hot = self.subreddit.hot(limit=lim)
        self.top = self.subreddit.top(limit=lim)
        self.rising = self.subreddit.rising(limit=lim)
        self.new = self.subreddit.new(limit=lim)
        res = res + "********" + "\n" + "Posts found in HOT" + "\n" + "********" + "\n" + "\n" + "\n"
        for sub in self.hot:
            if re.search(target,sub.selftext,re.IGNORECASE) != None or re.search(target,sub.title,re.IGNORECASE) != None:
                res = res + sub.title + "\t" + "Posted:  " + datetime.datetime.fromtimestamp(sub.created_utc).strftime('%Y-%m-%d %H:%M:%S') + "\n" + sub.url + "\n" + "\n" + "\n"
        res = res + "********" + "\n" + "Posts found in TOP" + "\n" + "********" + "\n" + "\n" + "\n"
        for sub in self.top:
            if re.search(target,sub.selftext,re.IGNORECASE) != None or re.search(target,sub.title,re.IGNORECASE) != None:
                res = res + sub.title + "\t" + "Posted:  " + datetime.datetime.fromtimestamp(sub.created_utc).strftime('%Y-%m-%d %H:%M:%S') + "\n" + sub.url + "\n" + "\n" + "\n"
        res = res + "********" + "\n" + "Posts found in RISING" + "\n" + "********" + "\n" + "\n" + "\n"
        for sub in self.rising:
            if re.search(target,sub.selftext,re.IGNORECASE) != None or re.search(target,sub.title,re.IGNORECASE) != None:
                res = res + sub.title + "\t" + "Posted:  " + datetime.datetime.fromtimestamp(sub.created_utc).strftime('%Y-%m-%d %H:%M:%S') + "\n" + sub.url + "\n" + "\n" + "\n"
        res = res + "********" + "\n" + "Posts found in NEW" + "\n" + "********" + "\n" + "\n" + "\n"
        for sub in self.new:
            if re.search(target,sub.selftext,re.IGNORECASE) != None or re.search(target,sub.title,re.IGNORECASE) != None:
                res = res + sub.title + "\t" + "Posted:  " + datetime.datetime.fromtimestamp(sub.created_utc).strftime('%Y-%m-%d %H:%M:%S') + "\n" + sub.url + "\n" + "\n" + "\n"
        
        return res