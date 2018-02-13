response = input("Enter a File Name: ")
list = [line.strip("\n") for line in open(response, 'r')
    if line.startswith('From') and not line.startswith('From:')]
sum = 0
count = 0

for line in list:
    if line.find("X-DSPAM-Confidence:") == -1:
        pass
    else:
        index = line.find(" ") + 1
        confidence = float(line[index:])
        sum += confidence
        count += 1
print("Average Spam Confidence: " + str(sum / count))