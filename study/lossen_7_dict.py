products = {
"T-Shirt": {"price": 300, "quantity": 10},
"Shirt": {"price": 250, "quantity": 20}, 
"Pants": {"price": 300, "quantity": 15}, 
"Shoes": {"price": 400, "quantity": 5}, 
"Socks": {"price": 25, "quantity": 7},
"Hat": {"price": 50, "quantity": 8},
"Gloves": {"price": 50, "quantity": 10},
"Sweater": {"price": 500, "quantity": 20},
"Jacket": {"price": 900, "quantity": 15}, 
"Coat": {"price": 1000, "quantity": 5},
"Scarf": {"price": 110, "quantity": 2}}

while True:
    product_name = input('Enter the product name \
(press Enter to Exit) : ').title()
    if product_name== '':
        break
    price_product = products.get(product_name,{}).get("price",'Not Available')
    quantity_product = products.get(product_name,{}).get('quantity','Not Available')
    massage = f'''Product : {product_name}
Price : {price_product}
Quantity : {quantity_product}'''
    print(massage)

print('Thanks for Choosing Codezilla ')


patients = {
"Mohamed Hassan": {"age": 25, "disease": "Cough", "room": 1},
"Ahmed Kamal":{"age": 30, "disease": "Sore Throat", "room": 2},
"Ali Adel": {"age": 35, "disease": "Arm Fracture", "room": 3},
"Hossam Yehia": {"age": 40, "disease": "ACL", "room": 4} }

while True:
    name_patient = input('Enter the peatient name \
(press Enter to Exit) : ').title()
    if name_patient == '':
        break
    age = patients.get(name_patient,{}).get('age','Not Available')
    disease = patients.get(name_patient,{}).get('disease','Not Available')
    room = patients.get(name_patient,{}).get('room','Not Available')
    print(f'''Patient : {name_patient}
Age : {age}
Disease : {disease}
Room : {room}
''')


inventory = {"Paracetamol": {"price":25, "quantity":10}, 
"Aspirin": {"price":15, "quantity":20},
"Ibuprofen": {"price":20, "quantity":15},
"Cough Syrup": {"price":30, "quantity":5},
"Augmentin": {"price":100, "quantity":7},
"Amoxicillin": {"price":80, "quantity":8}, 
"Panadol": {"price":25, "quantity":10},
"Zinc": {"price":15, "quantity":20}, 
"Vitamin C": {"price":20, "quantity":15}, 
"Fucidin": {"price":30, "quantity":5}, 
"Kolanog": {"price":100, "quantity":2},
}
    
names_treatment = input('Enter the treatnent seperated by comma \
(press Enter to Exit) : ').title().split(',')

if names_treatment :
     for name in names_treatment:
        price = inventory.get(name,{}).get('price','Not Available')
        quantity = inventory.get(name,{}).get('quantity','Not Available')
        print(f'''Item : {name}
Price : {price}
Quantity : {quantity}
          ''')
        print('-' * 20)
else:
    exit


students = {
    "Mohamed Hassan": {"grades": {
        "math": 100,
        "english": 90,
        "science": 80,
        "arabic": 100,
        "history": 97}
},
"Ahmed Kamal": {"grades": {
    "math": 100,
    "english": 95,
    "science": 93,
    "arabic": 100,
    "history": 94}
},
"Ali Adel": {"grades": {
    "math": 85,
    "english": 83,
    "science": 87,
    "arabic": 100,
    "history": 90}
},
"Hossam Yehia": {"grades": {
    "math": 100,
    "english": 94,
    "science": 98,
"arabic": 100,
        "history": 100}
    }
}

while True:

    name_student = input('Enter student name :\
(press Enter to Exit ) : ').title()
    if name_student == '':
        break
    name = students.get(name_student,{}).get('grades','no grades available')
    print(f'Student : {name_student}')
    if name != 'no grades available':
        for subject,grades in name.items():
            print(f'{subject} : {grades}')
    else:
            print(name)
            

