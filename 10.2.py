response = input('Enter File: ')
lines = [line.strip('\n') for line in open(response)
    if line.startswith('From ')]
dic = []
hourtotal = {}

for line in lines:
    email = line.split()[5]
    hour = email.split(':')[0]
    hourtotal[hour] = hourtotal.get(hour, 0) + 1
    
    for key in hourtotal:
        dic.append((key, hourtotal[key]))
      
    longest = sorted(dic)[0]

print(dic)
print(longest[1], longest[0])