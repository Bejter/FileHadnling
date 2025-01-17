import re

def count_vowels(text):
    pattern = r'[aoiueyAOIUYE]'
    total = 0
    for line in text:
        for char in line:
            if char in pattern:
                total += 1
    print(f'Number of vowels in your text equals: {total}')

text = input('Enter text to count: ')
count_vowels(text)