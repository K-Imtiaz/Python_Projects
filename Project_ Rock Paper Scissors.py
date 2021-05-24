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
game_images=[rock,paper,scissors  ]
user_choice=int(input("What do you want to choose?\ntype 0 for rock\ntype 1 for paper\ntype 2 for scissors\nType and 1 number between 0-2:  "))
if user_choice>=3 and user_choice<=0:
    print("You gave an invalid number! You lose!")  
else:
  print("User Chose")
print(game_images[user_choice])
computer_choice=random.randint(0, 2)
print(f"Computer chose:")
print(game_images[computer_choice])
  
if user_choice==0 and computer_choice==2:
    print("You Wins!")
elif user_choice==2 and computer_choice==0:
    print("You lose")    
elif computer_choice>user_choice:
    print("You lose")    
elif user_choice>computer_choice:
    print("You Win")    
elif computer_choice==user_choice:
    print("Its a draw!")

print("End of the game!")          
   

