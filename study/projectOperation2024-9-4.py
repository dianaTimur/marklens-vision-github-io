frist_num, operation, seced_num = input("Enter the operation: ").split()

if operation == "+":
    name_operation = 'Addition'
    result = float(frist_num) + float(seced_num)
elif operation == "-":
    name_operation = 'Subtraction'
    result = float(frist_num) - float(seced_num)
elif operation == "*":
    name_operation = 'Multiplication'
    result = float(frist_num) * float(seced_num)
elif operation == "/":
    name_operation = 'Division'
    result = float(frist_num) / float(seced_num)
elif operation == "**":
    name_operation = 'Exponentiation'
    result = float(frist_num) ** float(seced_num)
else:
    print("Invalid operation. Please use +, -, *, /, or **.")
print(f'{name_operation} result is : {result:,.2f}')

