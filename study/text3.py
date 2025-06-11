
# while True:
#     enter_input = input(">")
#     if enter_input.lower() == 'done':
#         break
#     elif len(enter_input) == 0:
#         continue
#     elif enter_input.startswith("#"):
#         continue
#     else:
        
#         print(enter_input)
     
# print("Done")




import random
end_mix = 0
number_random = random.randint(1,100)
while end_mix < 5  :
    guess_num = int(input('Guess the number '))
    if guess_num < number_random:
        print('Too low, try again ')
    elif guess_num > number_random:
        print('Too high, try again ')
    else:
        print('Your win')
        break
    end_mix += 1
print(f'You guessed the number in {end_mix} attempts, the number is win {number_random}')



# all_score = []
# while True:
#     score = input('Enter a score ( or type \'done\' to exit ) : ')
#     if score.lower() == 'done':
#         break
#     score = float(score)
#     all_score.append(score)
# average = sum(all_score) / len(all_score)
# if all_score:
#     print(f"The average or the score : {average:,.2f}")
# else:
#     print('Your don\t type anythig ! ')


item = []
index_item = 1
while True:
    name_product = input('Enter product name: ')
    if len(name_product) == 0:
        print('Thank you for shopping with Diana, Have a great day! ')
        break
    else:
        quantity = float(input('Enter quantity: '))
        price = float(input('Enter price: '))
        result = quantity * price
        print('-' * 20)
        print(f"Product : {name_product}")
        print(f'Quantity : {quantity}')
        print(f'Price : {price}')
        print('-' * 25)
        print(f'Total item cost : {result}')
        item.append(result)    
if item:        
    while index_item <= len(item):
            item.sort()
            print(f'Prices {index_item}: {item[-index_item]}')
            index_item += 1
    print('-' * 15)
print(f'Total cost : {sum(item)}')


# total = 1000
# while True:
#     user_input = input ("""Welcome to the ATM. Please select an option:
#             1. Check balance
#             2. Withdraw
#             3. Deposit
#             4. Exit
#                 Enter option number: \t""")
#     print('-' * 30)
#     if user_input == '1':
#         print(f'Your balance is ${total}')
#     elif user_input == '2':
#         withdraw_num = float(input('Enter withdraw amount: '))
#         if withdraw_num > total:
#             print('Insufficient balance')
#         else:
#             total = total - withdraw_num
#             print(f'Withdrawel successful. your new balance ${total}')
#     elif user_input == '3':
#         deposit_num = float(input('Enter deposit amount : '))
#         total += deposit_num
#         print(f'Deposit successful. your new balance is ${total}')
#     else:
#         print('Thank you for using the ATM. Have a great day. ')
#         break