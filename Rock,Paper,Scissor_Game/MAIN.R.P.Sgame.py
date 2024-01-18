import random
import math
print(
    "--------------------------------------------"
    """
    _______
---'   ____)
      (_____) 
      (_____) =ROCK
      (____)
---.__(___)
"""
    "--------------------------------------------"
    """
     _______
---'    ____)____
           ______)
          _______) =PAPER
         _______)
---.__________)
"""
    "-------------------------------------------"
    """
    _______
---'   ____)____
          ______)
       __________) =SCISSOR
      (____)
---.__(___)
"""
    "--------------------------------------------"
)
rock = """
    _______
---'   ____)
      (_____) 
      (_____) =ROCK
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______) =PAPER
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________) =SCISSOR
      (____)
---.__(___)
"""

game_images = [rock, paper, scissor]
user_choice = int(
    input("Enter (O for rock) , (1 for paper) and (2 for scissor).:"))

if user_choice > 2 or user_choice < 0:
    print("You entered invalid Input,Please Retry")
else:
    computer_choice = random.randint(0, 2)
    print(f"you choosed {game_images[user_choice]}")
    print(f"Computer choosed {game_images[computer_choice]}")

    # computer_choice=random.randint(0,2)
    print(f'computer choosed {computer_choice}')
    if computer_choice == user_choice:
        print("You and computer choosed same.It's a Draw")
    elif user_choice == 0 and computer_choice == 2:
        print("WoW you WIN")
    elif computer_choice == 0 and user_choice == 2:
        print("Ops you loosed")
    elif user_choice > computer_choice:
        print("WoW you WIN")
    elif computer_choice > user_choice:
        print("Ops you loosed")
    else:
        pass
    # elif user_choice>computer_choice:
    #     print("WoW you WIN")
    # elif computer_choice==0 and user_choice==2:
    #         print("Ops you loosed")
    # elif user_choice==0 and computer_choice==2:
    #     print("WoW you WIN")
    # else:
    #     print("Pease enter Vaid input")
