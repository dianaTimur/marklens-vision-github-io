import random
winner_1 = random.randint(1, 20)
winner_2= random.randint(1, 20)
winner_3 = random.randint(1, 20)
winner_4 = random.randint(1, 20)
list_winner = [winner_1, winner_2, winner_3, winner_4]

num = int(input("Enter a number between 1 and 20: "))
if not 1 <= num <= 20:
    print("Invalid input! Please enter a number between 1 and 20.")
elif num in list_winner:
    print( "You won!")
else:
    print(" You lost!")



import random
print('Guess the Roll Dice! ')
computer_num = random.randint(1,6)
num = int(input('Enter a number between 1 and 6: '))

print('-' * 15)
if not 1<= num <=6:
    print('Invalid input! Please enter a number between 1 and 6.')
elif num == computer_num:
    print(f"The Dice is {computer_num} ")
    print('Your won!')
else:
    print(f"The Dice is {computer_num} ")
    print('Your lost!')


import random
print('Guess the coin flip!')
num = int(input("""Enter 
      1 for Heads
      2 for Tails
      """))
print('-' * 12)

num_computer = random.randint(1,2)

if not 1<= num <= 2:
    print('Invalid input! Please enter 1 for Heads or 2 for Tails.')
    com = 0
elif num_computer == 1:
    com = 'Heads'
else:
    com = 'Tails'
if com:
    print(f"The Coin Flipped {com}")
    if num == num_computer:
        print('You won!')
    else:
        print('You lost!')
   