import sys
import random



name = input("What is your name?\n")
def run():
  print(f"Hello, {name}, let's play hangman!")
  print("Start guessing...")
  wordbank = ["Alabama",'Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
  'Illinos','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire'
  'New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont'
  'Virginia','Washington','West Virginia','Wisconsin','Wyoming']
  word = random.choice(wordbank).casefold()
  guesses = " "



  turns = 15 
  while turns > 0:
    failed = 0
    for char in word:
      if char in guesses:
        print(char)     
      else:
        print("*")
        failed += 1
    if failed == 0:
      print("You win!")
      choice = input("Would you like to play again? y/n\n")
      if "y" in choice:
        run()
      elif "n" in choice:
        sys.exit()
      else:
        print("Something went wrong, type y or n.")
        

    guess = input("Guess a character:")
    guesses += guess
    if guess not in word:
      turns -= 1
      print("Wrong!")
      print(f"You have {turns} more guesses.")
      if turns == 0:
        print("You lose!")
        
        choice = input("Would you like to play again? y/n\n")
        if "y" in choice:
          run()
        elif "n" in choice:
          sys.exit()
        else:
          print("Something went wrong, type y or n.")
run()

