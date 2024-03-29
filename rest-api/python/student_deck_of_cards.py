#!/usr/bin/env python
'''This was generated by 'Chukwubuikem Echeta' with the help of a POSTMAN generated code.
The variables, headers and methods were however used with the discretion of the author'''

import requests
from pprint import pprint

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
querystring = {
    "deck_count": "6"
}
payload = {}
headers = {
    'Cache-control':'no-cache',
    'Postman-Token': "dd1d8ca5-7000-21b2-2230-39969d585419"
}

response = requests.request("GET", url, headers=headers, data=payload, params=querystring)

print(response.text)

deck = response.json()
deck_id = deck["deck_id"]

url = "https://deckofcardsapi.com/api/deck/{}/draw/".format(deck_id)
querystring = {
    "count":"3"
}
secondResponse = requests.get(url, headers=headers, data=payload, params=querystring)
secondResponse = pprint(secondResponse.json())
print(secondResponse)
