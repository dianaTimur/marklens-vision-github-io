full_name = input("Enter your name").capitalize().split()

print("Hello, ", full_name[0],"Welcom at Age colculator")

day, month, year = input("Enter your birth date (dd-mm-yyyy)").split("-")
#1-11-2001
#day = 1 , month = 11 , year = 2001

Year = input("Enter your current year: ")

resolt = int(Year) - int(year)

print(f'Your age is : {resolt}')

#نفس الكود بشكل مختصر اكتر

name = input("Enter your name: ").capitalize().split()
dDay, dMonth, dYear = input("Enter your birth date (dd-mm-yyyy)").split("-")
date_year = input('Enter your current year: ')
print(f'Hello, {name[0]}\nWelcome at Age colculator\nYour age is : {int(date_year) - int(dYear)}')
