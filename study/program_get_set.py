# # available treatments
# inventory = {"Paracetamol": {"price":25, "quantity":10}, 
# "Aspirin": {"price":15, "quantity":20},
# "Ibuprofen": {"price":20, "quantity":15}, 
# "Cough Syrup": {"price":30, "quantity":5}, 
# "Augmentin": {"price":100, "quantity":7}, 
# "Amoxicillin": {"price":80, "quantity":8}, 
# "Panadol": {"price":25, "quantity":10},
# "Zinc": {"price":15, "quantity":20},
# "Vitamin C": {"price":20, "quantity":15}, 
# "Fucidin": {"price":30, "quantity":5}, 
# "Kolanog": {"price":100, "quantity":2}, }


    
# while True:
#     user_treatment = input('Enter treatment name \
#  (press Enter to Exit): ').title()
#     if user_treatment == '':
#         break
#     treatment = inventory.get(user_treatment)
#     if treatment:
#         for _ in treatment:
#             print(f'Item : {user_treatment}\nPrice : {treatment['price']}\nQuantity : {treatment['quantity']}')
#             break
#     else:
#         print('Not Available')
    

# employees = {
# "Mohamed Hassan": {"age": 25, "salary": 5000, "department":
# "HR"},
# "Ahmed Kamal": {"age": 30, "salary": 6000, "department":
# "IT"},
# "Ali Adel": {"age": 35, "salary": 7000, "department":
# "IT"},
# "Hossam Yehia": {"age": 40, "salary": 8000, "department":
# "IT"} }

# while True:
#     name_employee = input('Enter the employee name \
#  (press Enter to Exit) : ').title()
#     if name_employee == '':
#         break
#     employee = employees.get(name_employee)
#     if employee:
#         age,salary,department = employee.values()
#         print(f'''Employee : {name_employee}
# Age : {age}
# Salary : {salary}
# Department : {department}''')
#     else:
#         print('Not Available')



# students = {"Mohamed Hassan": {
	
# 		"Password": "123456",
	
# 		"grades": {
			
# 				"math": 100,
# 				"english": 90,
# 				"science": 80,
# 				"arabic": 100,
# 				"history": 97}},
# "Ahmed Kamal": {
	
# 		"Password": "1234",
		
# 			"grades": {
# 				"math": 100,
# 				"english": 95,
# 				"science": 93,
# 				"arabic": 100,
# 				"history": 94}},
# "Ali Adel": {
	
# 		"Password": "12",
	
# 		"grades": {
# 			"math": 85,
# 			"english": 83,
# 			"science": 87,
# 			"arabic": 100,
# 			"history": 90}},
# "Hossam Yehia": {
	
# 		"Password": "33",
	
# 		"grades": {
			
# 				"math": 100,
# 				"english": 94,
# 				"science": 98,
# 				"arabic": 100,
# 				"history": 100}}}

# while True:
#     student_name = input('Enter the student name \
#  (press Enter to Exit) : ').title()
#     student = students.get(student_name)
#     if student_name == '':
#         break
#     if student:
#         password = input('Enter The Password : ')
#         if student and password in student['Password']:
#             print('Grades .... ')
#             print('-' * 20)
#             for subject , grade in student['grades'].items():
#                print(f' {subject} : {grade} ')
#             list_number = list(student['grades'].values())
#             print(f'Student percentage {sum(list_number)/ len(list_number):.2f}%')
#     else:
#          print('Wrong password or student name ')


pharmacy_prices = {
    "panadol": 32,
    "cold free": 25,
    "omega 3": 45,
    "fuciden": 37,
    "augmentin": 50,
    "zinc": 20,
    "vitamin c": 15
}

your_pharmacy = {}


while True:
    user_pharmacy = input('Enter the names of treatments separated by a comma \
 (press Enter to Exit) : \n').lower().split(',')
    print('-' * 20)
    if user_pharmacy == [""]:
        break
    for word in user_pharmacy:
        found = pharmacy_prices.setdefault(word,'Not Available')
        your_pharmacy.update({word : found})
        print(f'{word} : {found}')
    print('-' * 20)
