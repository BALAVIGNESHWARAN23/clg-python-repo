#  1.Check Prime Number: Write a Java program that checks whether a given number is a prime number or not. (A prime number is only divisible by 1 and itself.)
num=int(input("enter a number to check whether a given number is a prime number or not: "))
count=0
for i in range(1,num):
    if num%i==0:
       
        count +=1
if count==1:
     print("it's prime")
else:
    print("it's not a prime" )


