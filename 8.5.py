response = input("Enter a File Name: ")
list = [line.strip("\n") for line in open(response, 'r')
    if line.startswith('From') and not line.startswith('From:')]

count = 0

for line in list:
    words = line.split()
    print(words[1])
    count += 1
    
print('There were %s lines in the file with From as the first word:' % (count))