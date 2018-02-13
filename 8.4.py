response = input('Enter File: ')
fhand = [line.strip('\n') for line in open(response)]
alphalist = []

for line in sorted(fhand):
    lines = sorted(response)
    words = line.split()
    for word in words:
        if word in alphalist:
            pass
        else:
            alphalist.append(word)
        
print(alphalist)