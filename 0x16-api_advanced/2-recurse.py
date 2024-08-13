#!/usr/bin/python3
"""
Task 0
"""
def recurse(subreddit, hot_list=[]):
    """
     a function that queries
     the Reddit API and prints the titles
     of the first 10 hot posts listed for
     a given subreddit.
    """
    import requests
    header = {"User-Agent": "My-User-Agent"}
    sub_reddit = requests.get("http://www.reddit.com/r/{}/hot.json"
                              .format(subreddit),
                              headers=header,
                              allow_redirects=False)
    if sub_reddit.status_code >= 400:
        return None
    hot = hot_list + [child.get("data").get("title")
                        for child in sub_info.json()
                        .get("data")
                        .get("children")]
    sub = sub_reddit.json()
    if not sub.get("data").get("after"):
        return hot
    return recurse(subreddit, hot, sub.get("data").get("count"),
                   sub.get("data").get("after"))