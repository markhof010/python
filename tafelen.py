user_input1 = input('please give a number of which you want to know the table of: ')
user_input2 = input('please give a number of the highest multiplier you want: ')
a = int(user_input1)
b = int(user_input2)

while (b > 0):
    result = b * a
    print(str(a) + ' * ' + str(b) + ' = ' + str(result))
    b = b - 1