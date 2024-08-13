#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    :param subreddit: The subreddit to query.
    :return: Number of subscribers or 0 if invalid subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'CustomUserAgent/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data'].get('subscribers', 0)
            return subscribers
        else:
            return 0
    except Exception:
        return 0
