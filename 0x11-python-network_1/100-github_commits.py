#!/usr/bin/python3
"""
Module to fetch and display the 10 most recent commits from a repository.
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'per_page': 10}

    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print('{sha}: {author_name}')
