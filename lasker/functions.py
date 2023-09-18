import requests
import chess.pgn
import chess.engine
import io
from html.parser import HTMLParser

url = 'https://lichess.org/api/games/user/' # API URL
username = 'R1206' # In the end username must be acquired from config file instead of hardcode. 
                   # The same goes for the url
engine = chess.engine.SimpleEngine.popen_uci(r'C:\Users\rfakhrutdinov\stockfish\stockfish-windows-2022-x86-64-avx2.exe') # Should be taken from config

def get_last_game_of_user(url, username): # returns PGN of a last game
    url = url + username
    g = requests.get(url, params={'max':1})
    if g.status_code != 200:
        raise Exception(f'Failed to retrieve the game. Status Code is {g.status_code}.')
    game = chess.pgn.read_game(io.StringIO(g.text))
    return game

def get_list_of_moves(game): # returns a list of moves
    moves = []
    for move in game.mainline_moves():
        moves.append(move)
    return moves

def is_best(move, board, engine, *args, depth=18, **kvargs): # checks if a move is the best
    evaluation = engine.analyse(board, chess.engine.Limit(*args, depth=18, **kvargs))
    return evaluation['pv'][0] == move