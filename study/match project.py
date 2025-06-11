cairo = ['Islam Mahfouz', 'Mohamed Mesilhy',
     'Hatem Elmaghraby', 'Kareem Embaby']
riyadh = ['Mohamed Gouda', 'Ayman Hamed',
     'Seif Ali', 'Adham Wael']
casablanca = ['Ahmed Ashraf', 'Abd El-Rahman Mahrous',
     'Islam Sheta', 'Mohamed Medhat', 'Mahmoud Nasser']
dubai= ['Ahmed Alaa', 'Kareem Abd-Elmeged',
     'Osama Ashraf', 'Mohamed Mostafa', 'Ahmed Bedeir']

name_offices = input("Enter the name of the office : ").lower()

match name_offices:
    case 'cairo' | 'egypt':
        join_offices = ", ".join(cairo[:-1])
        str_offices = f"The emloyees in {name_offices.upper()} are {join_offices} and {cairo[-1]}"
    case 'riyadh' | 'sauid arabia' | 'ksa':
        join_offices = ', '.join(riyadh[:-1])
        str_offices = f"The emloyees in {name_offices.upper()} are {join_offices} and {riyadh[-1]}"
    case 'casablanca' | 'morocco':
        join_offices = ', '.join(casablanca[:-1])
        str_offices = f"The emloyees in {name_offices.upper()} are {join_offices} and {casablanca[-1]}"
    case 'dubai' | 'uae':
        join_offices = ', '.join(dubai[:-1])
        str_offices = f"The emloyees in {name_offices.upper()} are {join_offices} and {dubai[-1]}"
    case _:
        str_offices = 0
        print('Not found ')
if str_offices:
    print(str_offices)
    