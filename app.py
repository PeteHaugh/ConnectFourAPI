import flask
from flask import request, jsonify
import json
from connect_four import evaluate_board, game_is_over, has_won, make_board, minimax, select_space

# PORT 5000

my_board = make_board()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return '<h1>Connect 4!</h1>'

#route to reset the board and start a new game
@app.route('/start', methods=['GET'])
def api_start():
    my_board = make_board()
    return f'{my_board}'
    
#route to move the piece for the player two to the desired column number,
#if the column is invalid return invalid else the move is valid,
#if there are four connecting pieces return Winner	

@app.route('/move/<col>', methods=['GET', 'POST'])
def make_move(col):
    # Check move is valid

    move = int(col)

    #The "O" player finds their best move
    valid = select_space(my_board, move, "O") #IF true it worked, if false it is invalid
    
    #Check if you've won

    if not game_is_over(my_board):
     #The "X" player finds their best move.
        result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), evaluate_board)
        select_space(my_board, result[1], "X")
        return f'{my_board}'
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