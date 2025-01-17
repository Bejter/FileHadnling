###
# Reads from file, line by line
#
x = 0
with open('countries.txt', 'r') as file:
    for line in file:
        x += 1
        print(f'{x}. {line}', end='')