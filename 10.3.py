file = input('Enter File: ')
book = open(file)


def letters(book):
    start = ('start')
    end = ('end')
    process = False
    lines = []
    allletters = ('')

    for line in book:
        if line.startswith(start) and process is False:
            process = True

        if line.startswith(end) and process is True:
            process = False

        if process is True:
            line = ''.join([char for char in line if char.isalpha()])
            line = line.lower()
            lines.append(line)

    allletters = allletters.join(lines)
    return allletters

condensed = letters(book)

letter_histogram = {}

for letter in condensed:
    letter_histogram[letter] = letter_histogram.get(letter, 0) + 1

results = []

for key in letter_histogram:
    results.append((letter_histogram[key], key))

print('Frequency results: ', file)
for pair in sorted(results, reverse=True):
    print(pair[1], pair[0])