menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120, "Meat Lovers Pizza": 150, "Chicken Pizza": 130, "Beef Burger": 100, "Chicken Burger": 80}
print(dir(menu))



while True:
    user_choice = input("""Enter your choice : 
                        1. Add new items
                        2. Remove items
                        3. Update items
                        4. Exit """)
    if user_choice == "1":
        name_item = input('Enter the name of the item to add to the menu (press Enter to Exit )').title()
        if name_item:
            price_item = float(input('Enter item price : '))
            new_item = {name_item : price_item}
            menu = menu | new_item
        else:
            continue
    elif user_choice == '2':
        name_item = input('Enter item name to be  deleted (press Enter to Exit )').title()
        if name_item in menu:
            done = input(f'Are you sure you wan\'t to delete {name_item} ? (Y / N)')
            if done.lower() == 'yes':
                del menu[name_item]
                print(f'{name_item} has been deleted')
            else:
                continue
        else:
            if name_item:
                print(f'{name_item} is not foud')
            else:
                continue
    elif user_choice == '3':
        name_item = input('Enter item name to be updated (press Enter to Exit ) : ').title()
        if name_item in menu:
            for item,price in menu.items():
                pass
            updated_price = float(input('Enter the new price : '))
            if updated_price:
                menu.update({item : updated_price})
                print(f'{name_item} has been updated ')
            else:
                continue
        else:
            if name_item is not menu:
                print(f'{name_item} is not foud')
            else:
                continue
    elif user_choice == '4':
         break

    else:
        print('Please Enter True numnber ... ')
        continue
if user_choice == '4':
    print('The New Menu : ')
    for item,price in menu.items():
        print(f'{item } : {price:.2f}')
        print('-' * 40)
        







