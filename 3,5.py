###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Wprowadz nazwe uzytkowanika: ')
password = input('Wprowadz haslo: ')

# pattern (criteria) for username and password
username_pattern = r'[a-z]{6,}'
password_pattern = r'[a-zA-Z0-9]{8,}'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print('Nazwa uzytkownika i haslo sa poprawne')
else:
   print('Nazwa uzytkownika lub/i haslo sa niepoprawne')