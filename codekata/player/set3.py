n=int(input("Enter the number:"))
rem=0
while(n>0):
    re=n%10
    rem=rem*10+re
    n=n//10
print(rem)
