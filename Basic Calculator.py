print("Operations:\n"
      "1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division")

oprn= int(input("\nSelect operation(1/2/3/4):"))
num1= int(input("\nEnter first number:"))
num2= int(input("Enter second number:"))

if oprn==1:
     print(num1,"+", num2,"=", num1+num2)
elif oprn==2:
    print(num1,"-", num2,"=", num1-num2)
elif oprn==3:
    print(num1,"*", num2,"=", num1*num2)
elif oprn==4:
    print(num1,"/", num2,"=", num1/num2)
else:
    print("Invalid input for operation")