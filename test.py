# from tictactoe import actions
# from tictactoe import player
# from tictactoe import result

import tictactoe

X = "X"
O = "O"
EMPTY = None

board=[[X, O, X],
       [EMPTY, X, EMPTY],
       [EMPTY, O, EMPTY]]
#
# print(actions(board))
# newset=actions(board)
# for x in newset:
#        print(result(board,x))
# rows = board + tictactoe.get_diags(board) + tictactoe.get_columns(board)
# print(rows)
print(tictactoe.minimax(board))
