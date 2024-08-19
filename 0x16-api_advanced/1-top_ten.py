#!/usr/bin/python3

"""Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    # Set the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set the headers with a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    
    try:
        # Send the GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the list of posts
            posts = data['data']['children']
            
            # Print the titles of the first 10 posts
            for post in posts:
                print(post['data']['title'])
        else:
            # If the subreddit is invalid, print None
            print(None)
    except Exception as e:
        # In case of any errors, print None
        print(None)
