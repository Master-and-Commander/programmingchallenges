# check the 'goodness' of a position in chess

## depends on

#number of pieces being attacked
#number of available pieces
#number of pieces that can be attacked (as well as which ones)
#mobility of each pieces
#number of pieces within vicinity of king and enemy king

#input array
def main(board, side):



# rating of how many pieces can be attacked
# weight 9
def attackableRating(board, side):
    return 4

# rating of the safetiness of the king
# weight 10
def kingRating(board, side):
    # analyse weaknesses
    # find if weaknesses are exploitable
    return 4

# rating of piece mobility
# weight 7
def mobilityRating(board, side):
    return 4

# rating of piece counts
# weight 8
def stats(board, side):
    return 4


def isEmpty(x,y, board):
    response = 1
    for i in arange(32):
        if board[i][0] == x and board [i][1] == y:
          response = 0
    return response




position = [ [0]*2 for i in range(32)]
side = "white"
# layout = wking, bking, wqueen, bqueen, wrook, brook, wbishop, bbishop, wknight, bknight, wpawn, bpawn ....

rating = main(position, side)
print(rating)
