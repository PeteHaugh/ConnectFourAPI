import flask
from flask import request, jsonify
import json
from connect_four import game_is_over, has_won, make_board, minimax, select_space
from script import my_evaluation_board, play_game

# PORT 5000

my_board = make_board()

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/')
def home():
    return '<h1>Connect 4!</h1>'

#route to reset the board and start a new game
@app.route('/start', methods=['GET'])
def api_start():
    #reset_board(my_board)
    return 'New game!'
    
#route to move the piece for the player two to the desired column number,
#if the column is invalid return invalid else the move is valid,
#if there are four connecting pieces return Winner	

@app.route('/move/<col>', methods=['GET', 'POST'])
def make_move(col):
    # Check move is valid

    move = int(col)

    #The "O" player finds their best move
    valid = select_space(my_board, move, "O") #IF true it worked, if false it is invalid

    # if not valid:
    #     return "invalid move"
    
    
    #Check if you've won

    if not game_is_over(my_board):
     #The "X" player finds their best move.
        result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluation_board)
        select_space(my_board, result[1], "X")
        return f'{result[1]}'
    elif has_won(my_board, "X"):
        return "X won!"
    elif has_won(my_board, "O"):
        return "O won!"
    else:
        return "It's a tie!"

    
def main():
    
    app.run()


if __name__ == "__main__":
    main()