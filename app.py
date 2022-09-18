import flask
from flask import request, jsonify
from flask_cors import CORS
import json
from connect_four import evaluate_board, game_is_over, has_won, make_board, minimax, select_space, reset_board

# PORT 5000

board = make_board()

app = flask.Flask(__name__)
CORS(app)

#route to reset the board and start a new game
@app.route('/start', methods=['GET'])
def api_start():
    reset_board(board)
    status = "Board reset"
    return jsonify(board, f"{status}")
    

@app.route('/move/<col>', methods=['GET'])
def make_move(col):

    move = int(float(col))

    #The "O" player finds their best move
    valid = select_space(board, move, "O") #IF true it worked, if false it is invalid
    
    #Check if you've won

    if not game_is_over(board):
     #The "X" player finds their best move.
        result = minimax(board, True, 4, -float("Inf"), float("Inf"), evaluate_board)
        select_space(board, result[1], "X")
        status = "Playing..."
    elif has_won(board, "X"):
        status =  "X won!"
    elif has_won(board, "O"):
        status =  "O won!"
    else:
        status =  "It's a tie!"

    return jsonify(board, f"{status}")

    
def main():
    app.run(host="0.0.0.0", port="5000", debug=True)


if __name__ == "__main__":
    main()