n = int(input("enter a number: "))
for i in range(n):
    print("*" * (i+1))

# other way to do this
for i in range(1,n+1):
    print("*" * i)