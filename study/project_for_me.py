nums = []
float_nums = []
name = input ('Please Enter your name : ')
while True:
    help_user = input('Enter anythig do you wint:( Enter space or Enter (exit)close the program)  ')
    if help_user.lower() == 'exit':
        print('Goodbya',name)
        break
    elif len(help_user) == 0:
        press_c_d= input ('Do you Calculator or Data type \n(You can writing Calculator or press 1) \n(You can writing Date type or press 2 )')
        if press_c_d.lower() == "calculator" or press_c_d == "1":
            while True:
                input_num = input('Enter a number ,Just finish Enter (done)')
                nums.append(input_num)
                
                if input_num == 'done':
                    
                    calculator = input('What process do you want ? ')
                    if calculator == "+":
                        nums.pop(-1)
                        for x in nums:
                            float_nums.append(float(x))
                        print(sum(float_nums))




   


