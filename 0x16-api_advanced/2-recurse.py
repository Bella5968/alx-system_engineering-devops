#!/usr/bin/python3
"""
Recursive function to fetch all hot post titles from a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to get all hot post titles from a subreddit.
    """
    if not subreddit:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "ALX-API-Advanced-Task-2"
    }
    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    if not data:
        return None

    children = data.get("children")
    for post in children:
        hot_list.append(post.get("data").get("title"))

    after = data.get("after")
    if after is not None:
        return recurse(subreddit=subreddit, hot_list=hot_list, after=after)

    return hot_list
