import random

# Display Current Board
def display_board(board):

  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('-----------')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('-----------')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


# Choose X or O
def player_input():
  marker = ''

  while marker != 'X' and marker != 'O':
    marker = input('[Choose X or O: ]').upper()

  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')



# Check who will go first?
def first_player():

  order = random.randint(0,1)

  if order == 0:
    return player1
  else:
    return player2

# Check player's mark
def marked_place(board, marker, position):

  board[position] = marker


# Check if there's any space available?
def space_available(board, position):

  return board[position] == ''

# Check if the board is full
def full_board(board):

  for i in range(1, 10):
    if space_available(board, i):
      return False

  return True

# Check the movement of the player
def players_move(board, player):

  position = 0

  while position not in range(1,10) or not space_available(board, position):
    position = int(input(f'[{player} Choose a position: (1-9)]'))
  
  return position


# Check the winner
def check_winner(board, marker):

  return((board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or (board[7] == board[8] == board[9] == marker) or (board[1] == board[4] == board[7] == marker) or (board[2] == board[5] == board[8] == marker) or (board[3] == board[6] == board[9] == marker) or (board[1] == board[5] == board[9] == marker) or (board[3] == board[5] == board[7] == marker))



# Check if the player wants to play again
def replay():

  answer = ''

  while answer != 'y' or answer != 'n':

    answer = input('[Play again? y/n]').lower()

    if answer == 'y':
      return True
    elif answer == 'n':
      return False




# Build the program

print('[Welcome to Tic Tac Toe!]')


# Start game
while True:

  the_board = [''] * 10

  player1, player2 = player_input()

  # Assign player

  player = {player1 : 'Player1', player2 : 'Player2'}

  turn = first_player()
  print('[' + turn + ' will go first!]')

  playgame = input('[Are you readey to play? y/n]').lower()

  if playgame == 'y':
    start_game = True
  else:
    start_game = False

  while start_game:

    if turn == player1:

      # Show board
      display_board(the_board)

      # Choose move

      position = players_move(the_board, player[player1])

      marked_place(the_board,player1,position)

      if check_winner(the_board, player1):

        display_board(the_board)

        print('[Player1 has won!!]')

        start_game = False
      
      else:

        if full_board(the_board):

          display_board(the_board)
          print('[Its a tie]')

          start_game = False

        else:

          turn = player2

    else:

      # Show board
      display_board(the_board)

      # Choose move

      position = players_move(the_board,player[player2])

      marked_place(the_board,player2,position)

      if check_winner(the_board, player2):

        display_board(the_board)

        print('[Player2 has won!!]')

        start_game = False
      
      else:

        if full_board(the_board):

          display_board(the_board)
          print('[Its a tie]')

          start_game = False

        else:
          
          turn = player1

  #Quit game?
  if replay() == False:
    break
   else: 
    player_replay

 
