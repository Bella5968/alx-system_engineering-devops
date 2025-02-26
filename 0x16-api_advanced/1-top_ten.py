#!/usr/bin/python3
"""Query Reddit API to print top 10 hot post titles."""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
headers = {"User-Agent": "custom-user-agent/1.0"}
response = requests.get(url, headers=headers, allow_redirects=False)
if response.status_code == 200:
    for post in response.json().get("data", {}).get("children", []):
    print(post["data"]["title"])
else:
    print(None)
