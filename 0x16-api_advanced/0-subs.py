#!/usr/bin/python3
"""
Task 0
"""
import requests # type: ignore
import json


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and
    returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit.
    If an invalid subreddit is given,
    the function should return 0
    """
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    header = {"User-Agent": "My-User-Agent"}
    sub_reddit = requests.get(url, headers=header, allow_redirects=False)

    if sub_reddit.status_code >= 300:
        return 0
    sub_reddit = sub_reddit.json()
    if sub_reddit.status_code == 200:  # Check for a successful response
        try:
            data = sub_reddit.json()  # Attempt to parse JSON
        except json.JSONDecodeError:
            print("Failed to parse JSON: Empty or invalid JSON content.")
    else:
        print(f"Request failed with status code {sub_reddit.status_code}")
    if 'data' in sub_reddit:
        return (sub_reddit.get('data').get('subscribers'))
    
    else:
        return 0
