#!/usr/bin/python3
"""
1-top_ten module
Fetches and prints the titles of the first 10 hot posts
from a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""

    # Set the User-Agent to avoid being blocked by Reddit
    headers = {'User-Agent': 'ALX-Advanced-API-Project'}

    # Build the URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Make the request (disable redirects to detect invalid subreddits)
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if subreddit is valid
    if response.status_code != 200:
        print(None)
        return

    # Parse JSON response
    data = response.json()

    # Extract posts and print titles
    try:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except (KeyError, TypeError):
        print(None)
