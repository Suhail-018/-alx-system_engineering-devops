#!/usr/bin/python3

"""Queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    # Set the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set the headers with a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditApp/0.1'}

    try:
        # Send the GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid, return 0
            return 0
    except Exception as e:
        # In case of any errors, return 0
        return 0
