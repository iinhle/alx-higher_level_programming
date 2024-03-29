#!/usr/bin/python3
'''
    Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API
    to display your id
'''
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    authan = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get('https://api.github.com/user', auth=authan)
    print(req.json().get('id'))
