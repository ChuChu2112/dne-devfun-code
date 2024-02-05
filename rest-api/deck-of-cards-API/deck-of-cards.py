import requests
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/")
responseData = response.json()
deckId = responseData["deck_id"]
if response.status_code == 200:
	print("It worked.")
	shuffleResponse = requests.get(f"https://deckofcardsapi.com/api/{deckId}/shuffle/")
else:
	print(f"Sorry, your request was unsuccessful, producing any erro message of {response.status_code}")
	exit()
	
# #another get request for 5 cards to be drawn
# parameters = {
# "count":5
# }
# drawResponse = requests.get(f"https://deckofcardsapi.com/api/{deckId}/draw/", param=parameters)
# drawData = drawResponse.json()

# #loop through the json object for drawn cards and print out each card's value and suit.
# for cards in drawData["cards"]:
# 	print(f"This is the card value: {cards[0]["value"]} and suit {cards[0]["suit"]})




# 	#
# 	#secondResponse = requests.get("https://deckofcardsapi.com/api/{{deckId}}/draw/?count=2
