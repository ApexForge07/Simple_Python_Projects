print('''This a program to tell greetings based on the time of the day.''')
import time
if time.localtime().tm_hour < 12:
    print("Good Morning!")
elif time.localtime().tm_hour >= 12 and time.localtime().tm_hour < 17:
    print("Good Afternoon!")
elif time.localtime().tm_hour >= 17 and time.localtime().tm_hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")
print("Have a nice day!")
a=str(input("Do you want to know the timestamp in 12-hour format? (y/n): "))
if a == "y":
    print("Current time in 12-hour format is: ", time.strftime("%I:%M:%S %p"))
else:
    print("Current time in 24-hour format is: ", time.strftime("%H:%M:%S"))
print("Thank you for using this program!")