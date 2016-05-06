"""
This program shows an implementation of the
tic-tac-toe game
"""

# Import library random to allow the computer to play
import random


def getBoard(dim_):
    """
    This function is intended to be used in an improved version of the code
    It is intended to generate square boards of any dimension
    :param dim_: number of rows (and cells) of the square board
    :return: list representing the board
    """
    return [' ']*(dim_**2 + 1)


def instructions(dim_):
    """
    This function displays the instructions for the user and gives her/him
    the option to be displayed again
    :return: Boolean value according to user's answer to question:
             do you want to see instructions again?
    """

    # We set show_instructions to True so that instructions gets displayed
    # at least once
    show_instructions = True

    # While show_instructions is True...
    while show_instructions:
        # Display information explaining how the user's moves should
        # be provided
        print "Welcome to the TIC TAC TOE game!"
        print "You will be shown a board as the following one"
        board_ = getBoard(dim_)
        drawBoard(board_)
        raw_input("Press any key to continue...")

        print "In order to make your move you will have to type"
        print "the digit corresponding to the position of the cell"
        print "in the board"
        print " "
        print "The position of cells is as follows..."
        board_ = [str(k) for k in range(10)]
        drawBoard(board_)
        print (" ")

        # We set ans_ so that in enters the while cycle at least once...
        ans_ = "x"
        # While the answer does not begin with "y" or "n" ...
        while (not ans_.startswith("y")) and (not ans_.startswith("n")) :
            # ... we keep asking the user if (s)he wants to see the
            # instructions again
            print("Do you want to see instructions again?")
            print("yes / no")
            ans_ = raw_input(' ').lower()
            show_instructions = ans_.startswith("y")

    # Return boolean user's answer
    return show_instructions


def chooseWeapon():
    """
    This function allows the user to choose either 'X' or 'O' to play
    tic-tac-toe. It informs the user if the symbol chosen is not allowed
    :return: list of two elements representing the symbols that will be
            used according the user's choice
    """
    print "Choose your weapon!"
    # Initialize symbol with an empty string
    symbol = " "
    # While the symbol is other than "X" or "O"...
    while not (symbol == "X" or symbol == "O"):
        # ... we ask the user to choose between the allowed symbols ...
        print "Select X or O "
        # ... and record the symbol provided ...
        key_ = raw_input(" ")
        # ... and capitalize it
        symbol = key_.upper()
        # If the symbol provided is neither "X" nor "O" ...
        if (symbol != "X") and (symbol != "O"):
            # ... we inform the user what symbol she/he chose and let her/him
            # know such a symbol is not allowed and ask her/him to try again
            print "Sorry my friend, " ,key_, "is not a valid option"
            print "Try again!"
        else:
            # If the symbol is allowed we are all set and the game begins
            print "Excellent! Here we go!"
    # Return list according the choice made by the user
    return ["X","O"] if symbol == "X" else ["O","X"]


def flipCoin():
    """
    This function randomly chooses whether the user or the computer
    will do the first move. In other words ... it "flips" a coin
    :return: entity who will start the game
    """
    # We simple generate a random number, 1 or 0, to choose who makes the first move
    return "user" if random.randint(0,1) == 1 else "computer"


def drawBoard(board):
    """
    This function prints the board to screen
    We have ignored the index '0' of the list to avoid
    confusion.
    The coding of this function has been intended to be
    "automatized" so that is can be used for boards larger
    than 3 X 3
    :param board: list representing the board
    :return: None (prints board to screen)
    """

    # Get length of array excluding the zeroth cell
    len_ = len(board) - 1
    # Length determines the size of the board by taking
    # square root
    dim_ = int(len_**(1./2))
    # Initialize row to printed to zero
    row_ = 0
    # Print upper boundary of board
    print('-----------')
    # While we have not exhausted the number of rows, which
    # will be increasing by dim_, we ...
    while row_ <= dim_*(dim_ - 1):
        # ... print internal vertical boundaries ...
        print('   |   |')
        print(''),
        # ... as well as the column corresponding to the row in turn,
        # except for the last cell ...
        for col_ in range(1,dim_):
            print(board[col_+row_] + ' |'),
        # which is printed out afterwards ...
        print '' + board[col_+1+row_]
        # ... along with the internal vertical boundaries of the
        # last cell ...
        print('   |   |')
        # ... followed by the lower boundary of the board
        print('-----------')
        # And we move on to the next row
        row_ += dim_


def makeMove(board, symbol, cell):
    """
    This function reads the move made by the user in turn (user or computer)
    and stores it in the in list representing the board in the corresponding
    cell (list entry)
    :param board: list representing the board
    :param symbol: weapon used by the user (either 'X' or 'O')
    :param cell: position of the list / board
    :return: None -- Only records move to the board
    """
    # We simply record the symbol in the corresponding board's cell
    board[cell] = symbol


def isCellAvailable(board, symbol):
    """
    This function returns a boolean value based on the availability
    of a cell to record a move
    :param board: list representing the board
    :param symbol: marker used by the user in turn ('X' or 'O')
    :return: True/False based on the availability of the cell
    """
    # We simply compute the boolean value corresponding to the availability
    # of the cell in the board
    return board[symbol] == ' '


def getUserMove(board):
    """
    This function reads the cell where the user is making her/his move
    It informs the user if the cell is already taken and allows her/his
    to try again until this is not so
    :param board: list representing the board
    :return: integer representing the cell in the board
    """
    # We populate an array with digits, in string format, representing the cells
    cells = [str(k) for k in range(1,10)]
    # Initialize the individual cell with an empty string
    cell_ = " "
    # While the individual cell provided, cell_, is not in the list
    # of allowed cells or the cell is not free...
    while cell_ not in cells or not isCellAvailable(board, int(cell_)):
        # We request the user her/his move ...
        print "What is your move? "
        # ... store it ...
        cell_ = raw_input(" ")

        # While the cell provided is not in the integer interval
        # [1,9] ....
        while cell_ not in cells:
            # ... we keep informing the user about the mistake
            # and show the board for (s)he
            print "Sorry my friend, that is not a valid cell"
            print "You have to provide a number between 1 and 9"
            print "Try again!"
            drawBoard(board)
            print "What is your move?"
            cell_ = raw_input(" ")

        # ... and check whether or not the cell is available.
        # If it is not available...
        if cell_ != " " and not isCellAvailable(board, int(cell_)):
            # We inform the user and gave him the chance to try again
            print "Sorry my friend, that cell is already taken"
            print "Try again!"
            drawBoard(board)
    # Return the cell in integer format
    return int(cell_)


def getRandomMove(board,movesList):
    """
    This function returns a valid move from the list on the passed board.
    It returns None in case there is no valid move.
    :param board: list representing the board
    :param movesList: list containing the valid moves
    :return:
    """

    # Initialize an empty list
    possibleMoves = []
    # Append all elements to possibleMoves from movesList
    for i in movesList:
        if isCellAvailable(board, i): possibleMoves.append(i)

    # In case the list of possibleMoves is not empty, return a random
    # choice from it. Otherwise return None
    return random.choice(possibleMoves) if len(possibleMoves) != 0 else None


def getComputerMove(board,computerSymbol):
    """
    This function determines the computer's move during the game. It intends to make
    a "smart" move based on the following rules:
    1. Checks if it can win the game in the next move. If so, provides such a move.
    2. Checks if the user can win the game in the next move. If so, blocks it.
    3. Checks if corners are available. If so, takes one of them.
    4. Checks if center is free. If so, takes it.
    5. Checks if cells adjacent to 5 are available. If so, takes one.
    :param board: list representing the board
    :param computerSymbol: symbol used by the computer
    :return: a "smart" move based on the previous rules
    """

    # We set computer's symbol based on user's symbol
    if computerSymbol == 'X':
        userSymbol = 'O'
    else:
        userSymbol = 'X'

    # We now start exploring the rules stated above:

    # Rule 1.- Computer checks if it can win in the next move
    # For all cells...
    for cell_ in range(1, 10):
        # We make a copy of the board to avoid mistakes with the
        # original board given
        boardCopy = [k for k in board]
        # We check if the cell in turn, cell_, is available
        if isCellAvailable(boardCopy, cell_):
            # If so, we make the move in the copyBoard
            # with the COMPUTER's symbol ...
            makeMove(boardCopy, computerSymbol, cell_)
            # ... check if such a move wins and ...
            if symbolWon(boardCopy, computerSymbol):
                # ... if so we return it
                return cell_

    # Rule 2. Check if the user could win on next move
    # For each cell ...
    for cell_ in range(1, 10):
        # We make a copy of the board (as before)
        boardCopy = [k for k in board]
        # If cell in turn, cell_, is available ...
        if isCellAvailable(boardCopy, cell_):
            # ... we make the move on the copy of the board
            # with the USER's symbol ...
            makeMove(boardCopy, userSymbol, cell_)
            # ... we check if this move (user's ) wins the game and ...
            if symbolWon(boardCopy, userSymbol):
                # ...if so we return it
                return cell_

    # Rule 3. Check if one of the corners is available
    # We make a random move to one of the corners to see if it allowed...
    move = getRandomMove(board, [1, 3, 7, 9])
    # ... if so ...
    if move != None:
        # ... computer returns it
        return move

    # Rule 4. Check if center is free
    # If center is free ...
    if isCellAvailable(board, 5):
        # ... computer returns it
        return 5

    # Rule 5. Check cells adjacent to '5' ...
    # ... and computer returns one of them
    return getRandomMove(board, [2, 4, 6, 8])


def isBoardFull(board):
    """
    This function provides a boolean answer to the question is the board full?
    If full, returns True. False otherwise
    :param board: list representing the board
    :return: False/True accordingly
    """
    # Return True if every space on the board has been taken. Otherwise return False.
    for k in range(1, 10):
        if isCellAvailable(board, k): return False
    return True


def symbolWon(board, symbol):
    """
    This function determines if the user using "symbol" won the game based
    on the board provided.
    It evaluates a boolean operation and it returns its result
    :param board: list representing the board
    :param symbol: symbol chosen by the user
    :return: boolean value: True if user won and False otherwise
    """

    # The following comparisons are self-explanatory and explore all possible
    # configurations by rows, columns and diagonals
    top_row = board[1] == symbol and board[2] == symbol and board[3] == symbol
    middle_row = board[4] == symbol and board[5] == symbol and board[6] == symbol
    bottom_row = board[7] == symbol and board[8] == symbol and board[9] == symbol
    left_column = board[7] == symbol and board[4] == symbol and board[1] == symbol
    middle_column = board[8] == symbol and board[5] == symbol and board[2] == symbol
    right_column = board[9] == symbol and board[6] == symbol and board[3] == symbol
    pos_diagonal = board[9] == symbol and board[5] == symbol and board[1] == symbol
    neg_diagonal = board[7] == symbol and board[5] == symbol and board[3] == symbol

    # return the boolean value based on the operation performed
    return (top_row or middle_row or bottom_row or left_column or middle_column or
            right_column or pos_diagonal or neg_diagonal)


def playAgain():
    """
    This function offers the user the choice of playing again
    :return: Boolean value according to the user's answer
    """

    ans_ = "x"
    while (not ans_.startswith("y")) and (not ans_.startswith("n")) :

        print("Do you want to play again?")
        print("yes / no")

        ans_ = raw_input(' ').lower()

    return ans_.startswith('y')


def manage_game(dim_):
    """
    This function executes the program that makes all the calls needed to play the game
    :return: Nothing
    """

    # A message announcing the game
    print('Let us play TIC TAC TOE!')

    while True:
        # This is intended to generalize the game in the future to allow the user
        # choosing the size of the board (N X N)
        # For the time being we only play a 3 X 3 game
        # Based on the dimension given, generate board
        board_ = getBoard(dim_)
        # By invoking chooseWeapon we determine what symbol the user chose
        userSymbol, computerSymbol = chooseWeapon()
        # Flip a coin to determine who makes the first move
        turn = flipCoin()
        # We let the user know who will go first
        print("The " + turn + " will move first.")

        # Boolean variable to determine if the game is over
        # Here we just initialize it (the game just started)
        isGameOver = False

        # While the game is NOT over...
        while not isGameOver:

            # In case is computer's turn ...
            if turn == 'computer':
                # ... we let it make its move...
                move = getComputerMove(board_, computerSymbol)
                # ... and register its move to the board
                makeMove(board_, computerSymbol, move)

                # Since we do not know "how long ago the game started", we have to
                # ask after every move if the user has won
                # So we ask if computer won:
                if symbolWon(board_ , computerSymbol):
                    # If it DID we draw the board ...
                    drawBoard(board_)
                    # ... and let the user know the bad news
                    print('The computer has beaten you! YOU LOST! :(.')
                    # We update the status of game to finalize it
                    isGameOver = True
                # If the computer DID NOT win then there are two possibilities...
                elif not symbolWon(board_ , computerSymbol):
                    # Either the board is full ...
                    if isBoardFull(board_):
                        # ... which means the game was a tie
                        drawBoard(board_)
                        print('This game was a TIE!')
                        # We update status of game to finalize it
                        isGameOver = True
                    # OR the board is not full and then is user's turn
                    elif not isBoardFull(board_):
                        turn = "user"

            # In case is user's turn...
            if turn == "user":
                # We draw the board ...
                drawBoard(board_)
                # ... request user's move ...
                move = getUserMove(board_)
                # ... and register the move to the board
                makeMove(board_, userSymbol, move)

                # Since we do not know "how long ago the game started", we have to
                # ask after every move if the user has won
                # So we ask if the user won ...
                if symbolWon(board_, userSymbol):
                    # ... if she/he DID we draw the board ...
                    drawBoard(board_)
                    # ... let the user know she/he won, we insult the computer ...
                    print('YOU WON! Take that computer!')
                    # ... and update the status of the game by setting the boolean
                    # variable to True to stop the game
                    isGameOver = True

                # If the user DID NOT, then there are two possibilities...
                elif not symbolWon(board_, userSymbol):
                    # Either the board is full and since the user DID NOT win...
                    if isBoardFull(board_):
                        # ... then the game was a tie ...
                        drawBoard(board_)
                        print('This game is a TIE!')
                        # ... and update the status of game
                        isGameOver = True

                    # If the board is not full and since the user DID NOT win then...
                    elif not isBoardFull(board_):
                        # ... the game is still on and it is the computer's turn
                        turn = 'computer'

        # We ask the user if he/she wants to play again ...
        if not playAgain():
            # ... and based on her/his answer we decide whether to stop
            # the game
            break

# To run the code itself...
if __name__ == '__main__':
    # IMPORTANT
    # For the time being this code runs only a typical
    # 3 X 3 tic-tac-toe game; it would be nice
    # to extend it to any square board of any size

    # We show instructions first and based on the last
    # question ...
    show_Instructions_Again = instructions(dim_=3)

    # we proceed to start the game
    manage_game(dim_=3)
