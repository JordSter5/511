response = input('Enter File: ')
lines = [line.strip('\n') for line in open(response)
    if line.startswith('From ')]
dic = {}

for line in lines:
    email = line.split()[1]
    dic[email] = dic.get(email, 0) + 1
    
    list = []
    for email in dic:
        list.append((dic[email], email))
      
    longest = sorted(list, reverse = True)[0]
#(sorted(list, reverse=True)[0])

print(dic)
print(longest[1], longest[0])