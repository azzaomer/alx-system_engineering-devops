#!/usr/bin/python3
"""
Task 0
"""


def top_ten(subreddit):
    """
     a function that queries
     the Reddit API and prints the titles
     of the first 10 hot posts listed for
     a given subreddit.
    """
    import requests
    header = {"User-Agent": "My-User-Agent"}
    sub_reddit = requests.get("http://www.reddit.com/r/{}/hot.json?limit=10"
                              .format(subreddit),
                              headers=header,
                              allow_redirects=False)
    if sub_reddit.status_code >= 300:
        return None
    else:
        [print(child.get("data").get("title"))
         for child in sub_reddit.json().get("data").get("children")]
