#!/usr/bin/python3
"""Module to query the Reddit API and print top 10 hot post titles."""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "custom-user-agent/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])

        for post in data:
            print(post["data"]["title"])
    else:
        print(None)
