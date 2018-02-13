response = input('Enter File: ') 
fhand = open(response)
count = 0
for line in fhand: 
    words = line.split()
    if len(words) == 0 or len(words[0:-1]) == 0 or words[0] != 'From' : continue
    print(words[2])