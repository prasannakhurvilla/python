y=input("Enter the Length of the array:")
x=input("Input:")
if y<=x:
    if(x<1 or (x%1)!=0):
        print("this is not a valid input")
    else:
        a=0
        while(x!=0):
            a=a+x
            x=x-1
        print "Output:",a
