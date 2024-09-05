# f = open("note.txt","rt")
# print(f.readlines())
# print(f.readline())
# for line in f:
#     print(line,end="")
# content = f.read()
# print(content)

# f.close()

# factorial of n = n*(n-1)! 

# def factorial(n):
#     number = int(input("Enter the number"))
#     for i in range(n):
#         fact = number * (i+1)
#     number-- 
# factorial()



s = 'F'
print(ord(s))

text = "Welcome to {a} {b} ".format(a="engineering", b = 12)
print(text)

text_new = "Welcome to {1} {0} ".format("engineering",12)
print(text_new)

text1 = "Welcome to {} {} ".format("engineering",12)
print(text1)

text12 = "Welcome to {b:>15} {a:5} ".format(b="engineering",a=12)
print(text12)

n = [m for m in range(1,10) if m % 2==0]
print(n)

s= "192"
l = [g for g in s]
print(l)