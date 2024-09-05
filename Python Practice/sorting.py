li =[7,8,3,6,4,5,4]
my_li=sorted(li,reverse=True) # sorted funct sort the list & returns a new list which should be stored in variable 
print('Sorted list is \t',my_li) 
li.sort(reverse=True) # sort() method sorts the list but returns none, hence it gives the same list, stored in same variable 
print(' list is \t',li)

tuple = (7,8,3,6,4,5,4)
s_tup = sorted(tuple)
print('Sorted tuple is:\t',s_tup)

dict = {"name":"Salman", 'corey':'schaffer','ajuu':'baba','jadugar':'zambora'}
c_dict = sorted(dict)
print("Sorted dict\t",c_dict)

li =[-7,-8,-3,6,4,5,4]
my_li=sorted(li,key=abs) 
print('Sorted list is \t',my_li) 
# li.sort(reverse=True) 
# print(' list is \t',li)

person = {'name':'Harshad','age':25}

# sentence = 'My name is {0} & age is {1}'.format(person['name'],person['age'])
# print(sentence)

# sentence = 'My name is {0[name]} & age is {1[age]}'.format(person,person)
# print(sentence)

sentence = 'My name is {0[name]} & age is {0[age]}'.format(person)
print(sentence)

l = ['jenny', 25]
sentence = 'My name is {0[0]} & age is {0[1]}'.format(l)
print(sentence)

sentence = 'My name is {name} & age is {age}'.format(name = 'jenn',age=23)
print(sentence)

sentence = 'My name is {name} & age is {age}'.format(**person) # unpack the dictionary values 
print(sentence)

for i in range(1,11):
    sentence = 'the value is {:03}'.format(i) # Zero padding
    print(sentence)

pi = 3.1456286
sentence = 'Pi value: {:.4f}'.format(pi)
print(sentence)

sentence = 'max value is: {:,.3f}'.format(1000**2)
print(sentence)

import datetime

mydate = datetime.datetime(2016,9,24,12,24,6)
print(mydate)

mydate = datetime.datetime(2016,9,24,12,24,6)
sentence = '{:%B %d, %Y}'.format(mydate)
print(sentence)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of a year'.format(mydate)
print(sentence)

