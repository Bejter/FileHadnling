###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name) as file:
   for line in file:
      if job_title in line:
         for words in line:
            print(f'{words}', end='')
            if words == ',':
               print(' ', end='')