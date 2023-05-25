import requests
from html.parser import HTMLParser

url = 'https://lichess.org/api/games/user/' # API URL
username = 'R1206' # In the end username must be acquired from config file instead of hardcode. 
                   # The same goes for the url

def get_last_game_of_user(url, username): # returns PGN of a last game
    url = url + username
    game = requests.get(url, params={'max':1})
    return game.text # Maybe it would be better if function returns a dictionary instead of string PDN
  # Must. Write. Tests.
