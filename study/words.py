import random

words = {
"Absence":"The lack or unavailability of something or someone.",
"Approval":"Having a positive opinion of something or someone.",
"Answer":"The response or receipt to a phone call, question, or letter.",
"Attention":"Noticing or recognizing something of interest.",
"Amount":"A mass or a collection of something",
"Borrow":"To take something with the intention of returning it after a period of time.",
"Baffle":"An event or thing that is a mystery and confuses.",
"Ban":"An act prohibited by social pressure or law.",
"Banish":"Expel from the situation, often done officially.",
"Banter":"Conversation that is teasing and playful.",
"Characteristic":"referring to features that are typical to the person, place, or thing.",
"Cars":"Four-wheeled vehicles used for traveling.", "Care":"extra responsibility and attention.",
"Chip":"a small and thin piece of a larger item.", "Cease":"to eventually stop existing.",
"Dialogue":"A conversation between two or more people.", "Decisive":"a person who can make decisions promptly.", }

attempt = True

while True:
    attempt = True
    choice = input('''1. Review answer
                      2. Test yourself
                      3. Exit
                   
                   Enter your choice : 
                    ''')
    if choice == '1':
        word , definition = random.choice(list(words.items()))
        print(f'{word} : {definition}')
    elif choice == '2':
        word , definition = random.choice(list(words.items()))
        print(f'Definition : {definition} ')
        while attempt:
            attempt_user = input('Enter the word : ').title()
            if attempt_user in words.keys():
                print('Correct answer')
                print('-' * 20)
                attempt = False
            else:
                print('Wrong answer you have 1')
                attempt_user = input('Enter the word : ').title()
                if attempt_user in words.keys():
                    print('Correct answer ')
                else:
                    print(f'Worng answer you have no more attemots ')
                    print(f'The correct answer is {word}')
                    attempt = False
    else:
        print('Hava a nice day ')
        break

