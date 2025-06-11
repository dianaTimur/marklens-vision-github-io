student_names = ["Mohamed", "Ahmed", "Ali", "Sara"]
student_grades = [[96, 78, 82, 80], [86, 92, 98, 90], [88 ,98 ,86 ,78] ,[72 ,90 ,88 ,76]]


for name , grades in zip(student_names,student_grades):
    print(f'Stufent : {name.capitalize()}')
    for grade in grades:
        print('Grades : ')
        print(grade , sep = ',')
