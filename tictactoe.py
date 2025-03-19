import random

class TicTacToe:
    """The game of Tic-Tac-Toe."""

    def __init__(self):
        """Initialize the game."""
        # This variable indicates whose turn is it.
        self.turn = ""
        # This variable indicates turn count.
        self.turn_count = 1
        # Set up the starting board. It will start with the spaces labeled from 1 to 9.
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # This variable indicates the winner, if there is one.
        # Assign to self.winner an empty string, which represents the scenario where there is no winner.
        self.winner = ""

    def who_goes_first (self):
        """Decide who goes first."""
        # If 1 is picked, O goes first; otherwise, X goes first. The value of self.turn is changed depending on who is chosen.
        first_move = random.choice([1, 2])
        if first_move == 1:
            self.turn = "O"
        else:
            self.turn = "X"
        print ("{} goes first.".format (self.turn))
    
    def display_board (self):
        """Display the board."""
        print ("{} {} {}".format (self.board[0], self.board[1], self.board[2]))
        print ("{} {} {}".format (self.board[3], self.board[4], self.board[5]))
        print ("{} {} {}".format (self.board[6], self.board[7], self.board[8]))
    
    def pick_space (self):
        """Player picks a space to fill with O or X."""
        # self.index indicates the item in self.board to change.
        # Use a try-except loop to make sure the player picks an eligible space in order to continue the game.
        while True:
            try:
                self.index = int (input ("It is {}'s turn. Enter a number: ".format (self.turn))) - 1
                # Make sure that if the player types an integer, it must be between 1 and 9.
                if self.index < 0 or self.index > 8:
                    print ("You need to pick an eligible space. Please try again.")
                    continue
                # Make sure that the player does not overwrite a space that is already taken.
                elif self.board[self.index] == "O" or self.board[self.index] == "X":
                    print ("That space is taken. Please try again.")
                    continue
                break          
            # This error occurs if the player enters a float number or something that is not a number.
            except ValueError:
                print ("You need to pick an eligible space. Please try again.")
    
    def fill_space (self):
        """Mark the chosen space with O or X, and record the move to tictactoe.txt."""
        # Replace the entered number with O or X.
        self.board[self.index] = self.turn
        # Record the move to tictactoe.txt.
        playbyplay = open ("tictactoe.txt", "a")
        playbyplay.write ("{}: {}\n".format (self.turn, str (self.index + 1)))
        playbyplay.close()

    def check_winner (self):
        """Check if there is a winner."""
        # If there is a winner, change the value of self.winner.
        # This function will return true or false for reasons explained later.
        if (self.board[0] == self.board[4] == self.board[8]) or (self.board[1] == self.board[4] == self.board[7]) or (self.board[2] == self.board[4] == self.board[6]) or (self.board[3] == self.board[4] == self.board[5]):
            self.winner = self.board[4]
            return True
        elif (self.board[0] == self.board[1] == self.board[2]) or (self.board[0] == self.board[3] == self.board[6]):
            self.winner = self.board[0]
            return True
        elif (self.board[2] == self.board[5] == self.board[8]) or (self.board[6] == self.board[7] == self.board[8]):
            self.winner = self.board[8]
            return True
        else:
            return False
    
    def next_turn (self):
        """Set up variables for the next turn."""
        if self.turn == "O":
            self.turn = "X"
        else:
            self.turn = "O"
        self.turn_count += 1

# Set up the game before it begins.
tictactoe = TicTacToe()
# Clear tictactoe.txt before the start of every game.
open ('tictactoe.txt', 'w').close()
# Decide who goes first.
tictactoe.who_goes_first()

# Play Tic-Tac_Toe. There can be a maximum of 9 turns.
while tictactoe.turn_count <= 9:
    # Display the updated board every turn for the players to see.
    tictactoe.display_board()
    tictactoe.pick_space()
    tictactoe.fill_space()
    # If check_winner returns true, it means there is a winner, and we have to break the loop to end the game.
    if tictactoe.check_winner():
        break
    # If there is no winner yet, set up for the next turn.
    tictactoe.next_turn()

# Display the results.
tictactoe.display_board()
if tictactoe.winner == "":
    print ("Nobody wins.")
else:
    print ("{} wins!".format (tictactoe.winner))