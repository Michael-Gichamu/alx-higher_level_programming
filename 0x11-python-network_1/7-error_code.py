#!/usr/bin/python3
"""
Sends a request to the URL and displays
the body of the response
If HTTP status code is >= 400
print error code
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    code = req.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(req.text)
