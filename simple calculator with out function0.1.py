def calculate():
    operation = input('''
please type in the math operation you like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('enter the first number'))
    number_2 = int(input('enter the second number'))

    if operation == '+':
        print('{} + {} = '.format(number_1,number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1,number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1,number_2))
        print(number_1 * nummber_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1,number_2))
        print(number_1 / number_2)

    else:
        print('you have not type a valid operator,please run the program again.')

 # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('good byeee.')
    else:
        again()

calculate()

