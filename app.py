import flask
from flask import request, jsonify
from flask_cors import CORS
import json
from connect_four import evaluate_board, game_is_over, has_won, make_board, minimax, select_space

# PORT 5000

my_board = make_board()

app = flask.Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return '<h1>Connect 4!</h1>'

#route to reset the board and start a new game
@app.route('/start', methods=['GET'])
def api_start():
    my_board = make_board()
    response = jsonify(message=f"Simple server is running, {my_board}")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    
#route to move the piece for the player two to the desired column number,
#if the column is invalid return invalid else the move is valid,
#if there are four connecting pieces return Winner	

@app.route('/move/<col>', methods=['GET'])
def make_move(col):
    # Check move is valid

    move = int(float(col))

    #The "O" player finds their best move
    valid = select_space(my_board, move, "O") #IF true it worked, if false it is invalid
    
    #Check if you've won

    if not game_is_over(my_board):
     #The "X" player finds their best move.
        result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), evaluate_board)
        select_space(my_board, result[1], "X")
        status = f'{my_board}'
    elif has_won(my_board, "X"):
        status =  "X won!"
    elif has_won(my_board, "O"):
        status =  "O won!"
    else:
        status =  "It's a tie!"

    response = jsonify(message=f"{status}")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

    
def main():
    app.run(host="0.0.0.0", port="5000", debug=True)


if __name__ == "__main__":
    main()