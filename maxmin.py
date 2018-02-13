def maxmin():
    L = 0
    S = 0
    response = []
    while True:
        number = input('Enter Number: ')
        if number == 'done':
            break
        
        try:
            def max(number):
                L = None
#                print('Before ', L)
                for x in number:
                    if L is None or x > L:
                        L = x
                return L
            def min(number):
                S = None
#                print('Before ', S)
                for y in number:
                    if S is None or y < S:
                        S = y
                return S
        except: 
            print('Invalid Input')
            continue
        number.append(response)
#    print(L , S)
    print('Maximum: ', max(number))
    print('Minimum: ', min(number))

maxmin()