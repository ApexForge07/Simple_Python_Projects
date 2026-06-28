import time
print('''This program will tell you the month and day of the week you were born on
It uses the time module to calculate the month and day of the week based on your birth date''')
y=int(input("Enter your Birth year in yyyy format: "))
m=int(input("Enter your Birth month in mm format: "))
d=int(input("Enter your Birth date in dd format: "))
# To convert the date into a time structure,
# we will use the f-string feature to format the date into a string and then use time.strptime() to convert it into a time structure.
date_of_birth = time.strptime(f"{y}-{m}-{d}", "%Y-%m-%d")
print('you were born in the month',time.strftime('%B', date_of_birth))
print('the day of the week you were born on is',time.strftime('%A', date_of_birth))
