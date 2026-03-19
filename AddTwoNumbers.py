num1=5
num2=3
print("sum:",num1+num2)
num1=float(input("enter first numbers:"))
num2=float(input("enter second numbers:"))
print("sum:",num1+num2)
try:
    num1=float(input("enter first numbers:"))
    num2=float(input("enter second numbers:"))
    print("sum:",num1+num2)
except ValueError:
    print("Please enter valid numbers.")
