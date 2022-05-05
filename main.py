import random

def diceRoll():
  return (random.randint(1,6))

player1 = diceRoll()
player2 = diceRoll()

print (f"Player 1 rolls a {player1}")
print (f"player 2 rolls a {player2}")

if player1 == player2:
  print(f"you both got a {player1}")
elif player1 > player2:
  print (f"Player 1 wins! ({player1} over {player2})")
else:
  print (f"Player 2 wins! ({player2} over {player1})")