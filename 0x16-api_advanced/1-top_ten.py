#!/usr/bin/python3
"""
Task 0
"""

import requests


def top_ten(subreddit):
    """
     a function that queries
     the Reddit API and prints the titles
     of the first 10 hot posts listed for
     a given subreddit.
    """

    url = ("https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit))
    header = {"User-Agent": "My-User-Agent"}
    reddit_response = requests.get(url, headers=header, allow_redirects=False)

    if reddit_response.status_code >= 300:
        return None
    response = reddit_response.json()
    if 'data' in response:
        for posts in response.get('data').get('children'):
            print(posts.get('data').get('title'))
    else:
        return (0)
