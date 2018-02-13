def minmax():
    response = []
    while True:
        try:
            user = input('Enter Number: ')
            user = int(user)
        except:
            break
        response = response + [user]
    print('Maximum: ', max(response))
    print('Minimum: ', min(response))
    
minmax()