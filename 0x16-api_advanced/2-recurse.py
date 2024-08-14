#!/usr/bin/python3
"""
Task 2
"""


import requests


def recurse(subreddit, hot_list=[]):
    """
     a function that queries
     the Reddit API and prints the titles
     of the first 10 hot posts listed for
     a given subreddit.
    """
    if type(subreddit) is list:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]
    header = {'User-Agent': 'CustomClient/1.0'}
    sub_reddit = requests.get(url, headers=header, allow_redirects=False)
    if sub_reddit.status_code >= 400:
        return None
    response = sub_reddit.json()
    if "data" in response:
        data = response.get("data")
        if not data.get("children"):
            return (hot_list)
        for post in data.get("children"):
            hot_list += [post.get("data").get("title")]
        if not data.get("after"):
            return (hot_list)
        subreddit[1] = data.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return (hot_list)
    else:
        return (None)
