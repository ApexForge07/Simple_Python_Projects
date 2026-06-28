print("This is a Calculator program.\nEnter two values one by one and then select the operation you want to perform.")
a=float(input("Enter the first value: "))
b=float(input("Enter the second value: "))
c=input("Enter the operation you want to perform (+, -, *, /): ")
while True:
    if c=='+':
        print(a, b, sep= c, end=" is equal to ")
        print(a+b)
        break
    elif c=='-':
        print(a, b, sep= c, end=" is equal to ")
        print(a-b)
        break
    elif c=='*':
        print(a, b, sep= c, end=" is equal to ")
        print(a*b)
        break
    elif c=='/':
        print(a, b, sep= c, end=" is equal to ")
        print(a/b)
        break
    else:
        print("Invalid operation selected.\nPlease choose from +, -, *, or /.")
    c=input("Enter the operation you want to perform (+, -, *, /): ")
    