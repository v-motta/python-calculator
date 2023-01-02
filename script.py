def calculate():
    oper = input('''Select the operator
    Please type:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    num1 = int(input("Write the first number: "))
    num2 = int(input("Write the second number: "))

    if oper == '+':
        print('{} + {}'.format(num1, num2))
        print(num1 + num2)
    elif oper == '-':
        print('{} - {}'.format(num1, num2))
        print(num1 - num2)
    elif oper == '*':
        print('{} * {}'.format(num1, num2))
        print(num1 * num2)
    elif oper == '/':
        print('{} / {}'.format(num1, num2))
        print(num1 / num2)
    else:
        print('Something wrong happened')

    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type y for YES or n for NO.
''')

    if calc_again.upper() == 'y':
        calculate()
    elif calc_again.upper() == 'n':
        print('See you later.')
    else:
        again()


calculate()
