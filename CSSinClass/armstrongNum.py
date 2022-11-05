num=int(input())

sum=0
while num>0:
    sum=(num%10)**2
    num=num//10
if sum==num:
    print("armstrong")
else:
    print("chutiya kat gya")



    