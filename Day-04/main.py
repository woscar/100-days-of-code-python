import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#list of images

game_images = [rock, paper, scissors]

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))

if user_choice >= 3 or user_choice <0:
  print("You typed a wrong number, please type 0, 1, or 2")
else:
  print("You chose:")
  print(game_images[user_choice])
  
  computer_choice = random.randint(0,2)
  print("Computer chose:")
  print(game_images[computer_choice])
  
  
  if user_choice == 0 and computer_choice ==2:
    print("You win!")
  
  elif user_choice == 1 and computer_choice ==0:
    print("You win!")
    
  elif computer_choice > user_choice:
    print("You lose!")
  
  elif user_choice == 2 and computer_choice ==0:
    print("You lose!")
  
  elif user_choice == 2 and computer_choice ==1:
    print("You won!")
    
  elif computer_choice == user_choice:
    print("It was a draw, play again")
    
  else:
    print("You typed a wrong number, please type 0, 1, or 2")
