n=int(input("enter the number:"))
s=len(str(n))
t=n
sum=0
while t>0:
    d=int(t%10)
    sum+=pow(d,s)
    t=t/10

if sum == n:
    print("armstrong")
else:
    print("not")
    
print("ascii code find:")
n=input("enter  the cha:")
a=ord(n)
print(f'{n} ascii code is ={a}')

print("decimal to others")
n=int(input("enter the decimal number"))
print(f'{n} is binary form of {bin(n)}, hexa form of{hex(n)}, octal form of {oct(n)}')

print ("/n list")
l=list()
n=int(input("range of list:"))
for i in range(n):
    l.append(int(input()))
print(l)    
