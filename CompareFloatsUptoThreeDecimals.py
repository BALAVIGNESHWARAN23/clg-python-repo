num1 = float(input("enter the first decimal number:"))
num2 = float(input("enter the second decimal number:"))

if round(num1, 3) == round(num2, 3):
    print("Equal up to three decimal places.")
else:
    print("Not equal up to three decimal places.")
