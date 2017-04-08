def power(a,b):
    ans = 1
    for i in range(b):
        ans *= a
    return ans
print("Enter base:",end=":")
a = int(input())
print("Enter exponent",end=":")
b = int(input())

print( power(a,b),a,"and",b,end="  ")
print(a+b,end="");


for i in range(1,a):
    for j in range(1,i+1):
        print("*",end="")
    print("")