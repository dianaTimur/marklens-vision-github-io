students = {
    "Mohamed Hassan": {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97},
        "school": "Codezilla"
    },
    "Ahmed Kamal": {"grades": {
"math": 100,
    "english": 95,
    "science": 93,
    "arabic": 100,
    "history": 94},
    "school": "Codezilla"
},
"Ali Adel": {"grades": {
    "math": 85,
    "english": 83,
    "science": 87,
    "arabic": 100,
    "history": 90},
    "school": "Al-Azhar"
},
"Sara Ahmed": {"grades": {
    "math": 100,
    "english": 94,
    "science": 98,
    "arabic": 100,
"history": 100},
        "school": "Al-Azhar"
    }
}


#student Name : Sara Ahmed
#school : Codezilla
#Grades: 
#Math : 100 ...
# --------
input_user = input('Please, Enter the name of the student : ').title()
if input_user  in students:
    print(f'{input_user} got the following grades : ')
    total = 0    
    for sub , grade in students[input_user]['grades'].items():

        print(f'{sub} : {grade}')
        
        total += grade
        averge = total / len(students[input_user]['grades'])
    print('-' * 20)
    print(f'{input_user}\'s total percentage is {averge:.2f}%')

else:
    print('The name is don\'t here ')
