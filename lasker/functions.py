import requests
import chess.pgn
import chess.engine
import io
from html.parser import HTMLParser

url = 'https://lichess.org/api/games/user/' # API URL
username = 'R1206' # In the end username must be acquired from config file instead of hardcode. 
                   # The same goes for the url
engine = chess.engine.SimpleEngine.popen_uci(r'C:\Users\rfakhrutdinov\stockfish\stockfish-windows-2022-x86-64-avx2.exe') # Should be taken from config

# returns PGN of a last game
def get_last_game_of_user(url, username): 
    url = url + username
    g = requests.get(url, params={'max':1})
    if g.status_code != 200:
        raise Exception(f'Failed to retrieve the game. Status Code is {g.status_code}.')
    game = chess.pgn.read_game(io.StringIO(g.text))
    return game

# returns a list of moves
def get_list_of_moves(game): 
    moves = []
    for move in game.mainline_moves():
        moves.append(move)
    return moves

# checks if a move is the best
def is_best(move, board, engine, *args, depth=18, **kvargs): 
    evaluation = engine.analyse(board, chess.engine.Limit(*args, depth=18, **kvargs))
    return evaluation['pv'][0] == move