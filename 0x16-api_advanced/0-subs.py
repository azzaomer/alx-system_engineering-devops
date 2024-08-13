#!/usr/bin/python3
"""
Task 0
"""
def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and
    returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit.
    If an invalid subreddit is given,
    the function should return 0
    """
    import requests
    header = {"User-Agent": "My-User-Agent"}
    sub_reddit = requests.get("http://www.reddit.com/r/{}/about.json"
                              .format(subreddit),
                              headers=header,
                              allow_redirects=False)
    if sub_reddit.status_code >= 300:
        return 0
    return sub_reddit.json().get("data").get("subscribers")