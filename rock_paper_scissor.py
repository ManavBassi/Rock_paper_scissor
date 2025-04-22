import random

options = [
"""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """,

  # Paper
"""
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
  """,

  # Scissors
"""
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """
]





computer_choice = random.choice(options)
computer_option = options.index(computer_choice)


user_choice = input("Choose rock, paper, or scissors: ")
user_option = ""
if user_choice == "rock":
  user_choice = options[0]
  user_option = options.index(user_choice)
elif user_choice == "paper":
  user_choice = options[1]
  user_option = options.index(user_choice)
elif user_choice == "scissors":
  user_choice = options[2]
  user_option = options.index(user_choice)
else:
  print("Invalid choice. Please choose rock, paper, or scissors.")

print("Computer chose:")
print(computer_choice)
print("You chose:")
print(user_choice)

if (user_option == 0 and computer_option == 2) or (user_option == 1 and computer_option == 0) or (user_option == 2 and computer_option == 1):
  print("You win!")
elif user_option == computer_option:
  print("It's a tie!")
else:
  print("Computer wins!")