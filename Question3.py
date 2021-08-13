def number(num1,num2,num3):
    if number1 > number2 and number1>number3:
        print(number1,"is greater")
    elif number2>number1 and number2>number3:
        print(number2,"is greater")
    else:
        print(number3,"is greater")

number1=int(input("Enter 1st Number"))
number2=int(input("Enter 2nd Number"))
number3= int(input("Enter 3rd Number"))
number(number1,number2,number3)