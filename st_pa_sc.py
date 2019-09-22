import random

user_input = input('please enter rock, paper of scissors: ')

Zetten = ['rock','paper','scissors']
pc = random.choice(Zetten)

a = 'Users choice: ' + user_input + '\n' + 'Random choice: ' + pc + '\nYou have lost'
b = 'Users choice: ' + user_input + '\n' + 'Random choice: ' + pc + '\nYou have won!!'

if (user_input == pc):
    print('Users choice: ' + user_input + '\n' + 'Random choice: ' + pc + '\nIt is a draw')

elif(user_input == 'rock'):
    if(pc == 'paper'):
        print(a)
    else:
        print(b)

elif(user_input == 'paper'):
    if(pc == 'scissors'):
        print(a)
    else:
        print(b)

elif(user_input == 'scissors'):
    if(pc == 'rock'):
        print(a)
    else:
        print(b)

else:
    print('You have put in an invalid word!')