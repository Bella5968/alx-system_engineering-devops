#!/usr/bin/python3
"""module to query the reddit api and print 10 hot post titles."""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "custom-user-agent/1.0"}

    response = requests.get(url, headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])

        for post in data:
            print(post["data"]["title"])
     else:
         print(None)
