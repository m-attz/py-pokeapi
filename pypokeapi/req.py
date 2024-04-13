#!/usr/bin/env python
import requests
import json

def send_request(url: str) -> None:
    try:
        response = requests.get(url).json()
        json_string = json.dumps(response, indent=4)
        return json_string
    except requests.exceptions.RequestException as e:
        return e
    

