'''
Saketh Katta
CSC110
Project -4
This program has eight functions which work together as a 
game of 1D chess.
'''
def create_board():
    '''
    This function creates a chess board
    Args:
        None
    Returns:
        A new chess board.
    '''
    chess = ["WKi", "WKn", "WKn", "EMPTY", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]
    return chess

row = ("+" + "-" * 53 + "+") # Creates a horizontal line for game display

def printable_board(chess):
    '''
    The components of a list are modified and organized in a structured manner
    provide a text based image of a board. It creates a distinct
    border for each empty area and visually represents a board based on the 
    information given in the first list.

    '''
    new = chess[:]
    for j in range(len(new)):
        if "EMPTY" in new[j]:
            new[j] = "   "
    return row + "\n" + '| ' + new[0] + " " + '| ' + new[1] + " " + '| ' + new[2] + " " + '| ' + new[3] + " " + '| ' + new[4] + " " + '| ' + new[5] + " " + '| ' + new[6] + " " + '| ' + new[7] + " " + '| ' + new[8] + " |" + "\n" + row

def is_valid_move(chess, place, player):
    '''
    Checks if a move on the board is valid.
    Args:
        chess: The current state of the 1D chess board.
        place: The position being considered for the move.
        player: The player making the move.
    Returns:
        True if the move is valid, otherwise False.
    '''
    if 8 >= place >= 0: # Checks if the place is within the range of the board
        if chess[place][0] == player[0]:
            return True # Returns True if move is valid
        elif chess[place][0] != player[0]:
            return False # Returns False if move is invalid
    else: 
        return False # Returns False if move is invalid

def move_king(chess, place, path):
    '''
    Moves the king piece in the 1D chess game.
    Args:
        chess: The current state of the 1D chess board.
        place: The position of the king piece.
        path: The direction in which to move the king.
    Returns:
        The updated 1D chess board after moving the king piece.
    '''
    if path == "RIGHT":
        if chess[place][0] == "W":
            for j in range(1, len(chess)):
                if chess[place + j] != "EMPTY":
                    chess[place + j] = chess[place]
                    chess[place] = "EMPTY"
                    return chess
        else: 
            return chess
    elif path == "LEFT":
        if chess[place][0] == "B":
            for j in range(1, len(chess)):
                if chess[place - j] != "EMPTY":
                    chess[place - j] = chess[place]
                    chess[place] = "EMPTY"
                    return chess
        else:
            return chess
            
def move_knight(chess, place, path):
    '''
    Moves the knight piece in the game.
    Args:
        chess: The current state of the 1D chess board.
        place: The position of the knight piece.
        path: The direction in which to move the knight.
    Returns:
        The changed chess board after moving the knight.
    '''
    if path == "RIGHT":
        chess[place + 2] = chess[place]
        chess[place] = "EMPTY" # Moves the knight and empties the previous position
        return chess
    elif path == "LEFT":
        chess[place - 2] = chess[place]
        chess[place] = "EMPTY" # Moves the knight and empties the previous position
        return chess

def move(chess, place, path):
    '''
    Initiates the move of a piece on the 1D chess board.
    Args:
        chess: The current state of the 1D chess board.
        place: The position of the piece to be moved.
        path: The direction in which to move the piece.
    Returns:
        The changed 1D chess board after the piece is moved.
    '''
    if chess[place] == "BKn" or chess[place] == "WKn":
        move_knight(chess, place, path) # Calls the move_knight function for knight piece
        return chess
    elif chess[place] == "WKi" or chess[place] == "BKi":
        move_king(chess, place, path) # Calls the move_king function for king piece
        return chess
    return chess

def is_game_over(chess):
    '''
    Checks if the game is over by checking the presence of kings on the board.
    Args:
        chess: The current state of the 1D chess board.
    Returns:
        True if the game is over, otherwise returns False.
    '''
    if "BKi" not in chess:
        return True # Returns True if black king is absent
    elif "WKi" not in chess:
        return True # Returns True if white king is absent
    elif "WKi" in chess and "BKi" in chess:
        return False # Returns False if both kings are present

def whos_the_winner(chess):
    '''
    Finds out the winner of the chess game.
    Args:
        chess: The current state of the 1D chess board.
    Returns:
        'Black' if black wins and 'White' if white wins. Otherwise it returns none
    '''
    if "WKi" not in chess:
        return "Black" # Returns 'Black' if white king is absent
    elif "BKi" not in chess:
        return "White" # Returns 'White' if black king is absent
    else:
        return None # Returns None if both kings are present