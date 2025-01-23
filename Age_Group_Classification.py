# 2.Age Group Classification: Write a Java program that takes an age as input and prints the corresponding age group:

# 0-12: Child
# 13-19: Teenager
# 20-64: Adult
# 65 and above: Senior

age=int(input("enter a age: "))
if(age>=0 and age<=12):
    print("child")
elif(age>=13 and age<=19):
    print("Teenager")
elif(age>=20 and age<=64):
    print("Adult")
elif(age>=65):
    print("Senior")

