def maxmin():
    L = 0
    S = 0
    x = 0
    y = 0
    while True:
        number = input('Enter Number: ')
        if number == 'done':
            break
        else:
            try:
                L = int(number)
                if x > L:
                    L = X
                if Y == 0:
                    S = L
                if x < S:
                    S = x
                y = y + 1
            except:
                print('Invalid Input')
                continue
        print(L , S)