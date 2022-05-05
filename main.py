import random

def diceRoll():
  return (random.randint(1,6))

player1 = diceRoll()
player2 = diceRoll()

print (f"Player 1 rolls a {player1}")
print (f"player 2 rolls a {player2}")