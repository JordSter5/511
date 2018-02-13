def minmax():
    numbers = []
    count = 0
    while True:
        collect = input('Enter a Number: ')
        if collect == 'done':
            print min(numbers), max(numbers)
            break
        else:
            print('invalid input')
minmax()
