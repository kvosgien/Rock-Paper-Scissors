
player1 = 'rock'
player2 = 'scissors' 

# tie
if player1 == player2:
  print("It's a tie!")
# player 1 = scissors
elif player1 == 'scissors':
  if player2 == 'rock':
    print("Player 2 wins!")
  elif player2 == 'scissors':
    print("Player 1 wins!")
# player 1 = rock
elif player1 == 'rock':
  if player2 == 'scissors':
    print("Player 1 wins!")
  elif player2 == 'rock':
    print("Player 2 wins!")
# player 1 = scissors
elif player1 == 'scissors':
  if player2 == 'rock':
    print("Player 2 wins!")
  elif player2 == 'rock':
    print("Player 1 wins!")