import requests
import chess.pgn
import io
from html.parser import HTMLParser

url = 'https://lichess.org/api/games/user/' # API URL
username = 'R1206' # In the end username must be acquired from config file instead of hardcode. 
                   # The same goes for the url

def get_last_game_of_user(url, username): # returns PGN of a last game
    url = url + username
    g = requests.get(url, params={'max':1})
    if g.status_code != 200:
        raise Exception(f'Failed to retrieve the game. Status Code is {g.status_code}.')
    game = chess.pgn.read_game(io.StringIO(g.text))
    return game
