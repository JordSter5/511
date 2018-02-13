def adding():
    total = 0
    count = 0
    while True:
        number = input('Enter a Number: ')
        if number == 'done':
            break
        else:
            try:
                total = int(number)
                count = count + total
            except: 
                print('Invalid Input')
                continue
    print(total, count, total/count)

adding()
