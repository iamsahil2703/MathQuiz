import random
import datetime
pattern = input('Enter the problem type (i.e., 10+20 means [0-10]+[0-20]): ')
if pattern == '':
    pattern = '10+10'
if '+' in pattern:
    op = '+'
elif '-' in pattern:
    op = '-'
elif '*' in pattern:
    op = '*'
elif '/' in pattern:
    op = '/'
left_limit = int(pattern.split(op)[0].strip())
right_limit = int(pattern.split(op)[1].strip())
rights = wrongs = 0
while True:
    a = random.randint(0 if op != '/' else 1, left_limit)
    b = random.randint(0 if op != '/' else 1, right_limit)
    if op in ['-', '/']:
        a, b = max(a, b), min(a, b)
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    question = '\n' + ' '.join([str(a), op, str(b), '= '])
    answer = input(question)
    if int(answer) == result:
        rights += 1
        print("Right!")
    else:
        wrongs += 1
        print("Wrong!")
    again = input('Again? ')
    if again.lower() in ['no', 'n']:
        score = str(rights) + ' right, ' + str(wrongs) + ' wrong.'
        print('\nYour score:', score)
        break
