n=int(input("Enter the number which you want print the factorial:"))
r=n
for i in reversed(range(1,n)):
    n=n*i
print("The factorial value of",r,"is:",n)
