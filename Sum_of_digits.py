get_num=int(input("enter the digits to sum :"))
sum=0
while(get_num>0):
    sum+=get_num%10
    get_num//=10
print(sum)