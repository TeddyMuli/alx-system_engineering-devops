#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/TedMAMBA)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("Error: Received status code {}".format(response.status_code))
        return 0
    
    try:
        # Attempt to parse JSON
        results = response.json().get("data")
        return results.get("subscribers", 0)
    except ValueError:
        # If parsing fails, print the response text for debugging
        print("Error: Unable to parse JSON. Response text: {}".format(response.text))
        return 0