#!/usr/bin/python3
"""
Takes URL and displays the value of the variable X-Request-Id
in the response header
"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(f"{sys.argv[1]}")
    print(req.headers.get("X-Request-Id"))
