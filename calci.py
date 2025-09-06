def calc(first, method, second):
    answer = 0
    if method == '+':
        answer = first + second
    elif method == '-':
        answer = first - second
    elif method == '*':
        answer = first * second
    elif method == '/':
        answer = first / second
    else:
        answer = 'Command not found'
    print(answer)


isOpen = True
while(isOpen):
    print('Write: ')
    list = input().split()
    first = list[0]
    method = list[1]
    second = list[2]
    print('answer: ' + calc(float(first), str(method), float(second)))
    
