# def hello(greet, name = 'You'):
#     return '{} {}'.format(greet,name)
# # print(hello('Hi'))

# def student(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ['Math','Art']
# info = {'name':'Python'}
# student(*courses , **info)

# import os

# print(os.getcwd)

greet = "swagat"
game = "changer"
# name = "{}, {} welcome home".format(greet,game)
name = f"{greet}, {game.upper()} welcome home"
print(name)

# a = 7
# print(dir(a))

print(help(str.upper))

my_list = [1,3,5,7,9,20,6,74,5]
print(my_list[7:1:-2]) 

sample_url = "https://muquestionpapers.com/be/electronics-and-telecommunication/semester-7"
print(sample_url[::-1])


# List comprehension: 
mylist=[1,2,3]
emp=[]
for i in mylist:
    emp.append(i)
print(emp)

mylist2=[1,2,3]
emp2=[i for i in mylist]
print(emp2)

mylist4=[1,2,3]
emp4=[]
for i in mylist4:
    emp4.append(i*i)
print(emp4)

mylist3=[1,2,3]
emp3=[i*i for i in mylist3]
print(emp3)


mylist5=[1,2,3]
emp5=[]
for i in mylist5:
    if(i%2==0):
      emp5.append(i)
print(emp5)

mylist6=[4,5,6]
emp6=[n for n in mylist6 if n%2==0]
print(emp6)
