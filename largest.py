x=int(input("Enter the no. "))
y=int(input("Enter the no. "))
z=int(input("Enter the no. "))
if (x>y and x>z):
    print(x, " is largest")
elif(y>x and y>z):
    print(y, " is largest")
else:
    print(z, " is largest")
a=max(x,y,z)
print(a," is largest")