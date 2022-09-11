from connect_four import *

def my_evaluation_board(board):
  if has_won(board, "X"):
    return float("Inf")
  if has_won(board, "O"):
    return -float("Inf")
  x_two_streak = 0
  o_two_streak = 0

  for col in range(len(board) - 1):
    for row in range(len(board[0])):
      if board[col][row] == 'X'and board[col + 1][row] == 'X':
        x_two_streak += 1
  for col in range(len(board) - 1):
    for row in range(len(board[0])):
      if board[col][row] == 'O' and board[col + 1][row] == 'O':
        o_two_streak += 1
  
  return x_two_streak - o_two_streak


