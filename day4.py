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
import random
hands_list=[rock,paper,scissors]
user_inp = int(input("Rock(0)/Paper(1)/Scissors(2)::\n"))
print("You chose:\n",hands_list[user_inp])

hand_type = [0,1,2]

computer_choice = random.choice(hand_type)
print("Computer chose:\n",hands_list[computer_choice])

if user_inp == 0:
    if computer_choice == 0:
        print("Draw")
    elif computer_choice == 1:
        print("You lose..")
    elif computer_choice == 2:
        print("You win!!!")
elif  user_inp == 1:
    if computer_choice == 0:
        print("You win!!")
    elif computer_choice == 1:
        print("Draw..")
    elif computer_choice == 2:
        print("You lose..")
elif  user_inp == 2:
    if computer_choice == 0:
        print("You lose..")
    elif computer_choice == 1:
        print("You win!!")
    elif computer_choice == 2:
        print("Draw")