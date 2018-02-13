lines = [word.strip('\n') for word in open('words.txt')]
dic = {}
for line in lines:
    words = line.split()
    for word in words:
        dic[word] = 0
print(dic)