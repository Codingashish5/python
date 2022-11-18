import operator
import math
import array
import array as arr


# import keyword
# num1 =  int (input("enter num1: "))
# # print("welcome ",num1);
# num2 = int(input("enter num2:"))
# num3 =num1*num2
# print ("product is:" , num3)
# num1 =int(input("enter num:"))
# if(num1>35):
#     print("number is not good....")
# elif(num1>12):
#     print("number is good")
#
# else:
#     print("number is great")
#

# def ashish():
#     print("ashish")
#     print("welcome ashish")
# ashish()
#
#
# def ma():
#     num = -85
#     num = math.fabs(num)
#     print(num)
#
# ma()
#
# def getinterger():
#  result = int(input("enter interger:"))
#  return result
#
# # def ma():
# #     print("started")
# #     output = getinterger()
# #     print(output)
# #     ma()
#
#
# # for step in range(5):
# #     print(step)
#
#
# myNumber = 3
# print(myNumber)
# myNumber2 = 4.5
# print(myNumber2)
# myNumber = "helloworld"
# print(myNumber)
#
#
#
# nums = []
# nums.append(21.5)
# nums.append(40.6)
# nums.append("string")
# print(nums)
#
#
#
# # input and output
#
# # name = input("enter your name:")
# # print("hello", name)
# #
# # print("the list of keyword is :")
# # print(keyword.Kwlist)
#
#
# print(False == 0)
# print(True == 1)
#
# print(True+True+False   )
# print(True+False+False)
# print(None == 0)
# print(None == [])
#
#
#
# print(True or  False)
# print(False or True)
# print(not True)
#
# if 'h 'in 'ashish':
#     print("h is a part of ashish")
# else:
#     print("h is not a part of ashish")
#
#     for i  in 'ashish':
#         print(i,end = " ")
#         print("\r")
#         print(''is'')
#         print({} is {} )
#
#         for i in range (10):
#             print(i,end = " ")
#             if i == 6:
#                 break
# print()
# i=0
# while i < 10:
#     if i == 6:
#         i+=1
#         continue
#     else:
#         print(i,end = " " )
#         i += 1
#
#
# def fun():
#     s = 0;
#     for i in range(10):
#         s +=1
#     return s
# print(fun())
# def fun():
#         S =  0
#         for i in range(10):
#             S += i
#             yield S
#
#
#
#
# for i  in fun():
#          print (i)
#
# j=1
# while(j<=5):
#     print(j)
#     j=j+1
#
#
#
# # taking input in python
#
# val = input("enter your value:")
# print(val)
#
# name = input('what is your name?\n')
# print (name)
#
# num = input("enter number:")
# print(num)
# name1 = input("enter name:")
# print (name1)
# print("type of number",type(num))
# print("type of name",type(name1))

# input frm console in python

# num1 = int(input("Enter any value"))
# num2 = int(input("Enter any value 2 -"))
# print(num1+num2)

# split() method
# x , y = input("enter two values:").split()
# print("number of boys:", x )
# print("number of girls:", y)
# print()
# x , y , z = input("Enter three values:").split()
# print("total number of student :", x)
# print("total number of boys is :", y)
# print("total number of girls is :", z)
# print()
# a , b = input("enter two values:").split()
# print("First number is{} and second number is {}".format(a,  b))
# print()
# x = list(map(int, input("enter multiples value:").split()))
# print("list of student:",x)


print("python")
# print("python for python")
# array
a =[1, 2, 3, 4, 5]
for i in range(4):
    print(a[i],end =" ")
print("")
    # Arithmetic# Operators
a = 9
b = 5
add = a +b
sub = a - b
mul = a * b
div1 = a / b
div2 = a // b
mod = a % b
p = a ** b
# print result

print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)
print("")

# Relational Operators
# > greater than
# < lesser than
a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print("")
# Logical Operator

a = True
b = False
print(a and b)
print(a or b)
print(not a)
print("")

# Bitwise Operators
a = 10
b = 4
print(a & b)
print(a | b)
print(~ a)
print(a ^ b)
print(a >> 2)
print(a << 2)
print("")

# Assignment Operators
a = 10
b = a
print(b)
b +=  a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)
print("")

# Identity Operators
a = 10
b = 20
c = a
print(a is not b)
print(a is c )
# Operator Overloading

print(1+2)
print("ashish"+"mundra")
print(3 * 4)
print("ashish" * 5 )

# operators
a = 4
b=  3
print("the addition of number is :",end="");
print(operator.add(a, b))
print("the differnce of number is :",end="");
print(operator.sub(a, b))
print("the product of number is :",end="");
print(operator.mul(a, b))
print("the moduls of number is :",end="");
print(operator.mod(a, b ))
print("")
#
a = 3
b = 4
if(operator.lt(a, b)):
    print("3 is less than 3")
else:print("3 is not less than 3")
if(operator.le(a, b)):
    print("3 is less than or equal to 3")
else:print("3 is not less than or equal to 3")
if(operator.eq(a, b)):
    print("3 is equal to 3 ")
else:print("3 is not equal to 3")
print("")


#  concat(obj1,obj2) :- This function is used to concatenate two containers.
# Operation – obj1 + obj2
# contains(obj1,obj2) :- This function is used to check if obj2 in present in obj1.
# Operation – obj2 in obj1

s1 = "ashish"
s2 = "mundra"
# concate
print("the concatenated string is :", end="")
print(operator.concat(s1, s2))
# contain
if operator.contains(s1, s2):
    print("ashish mundra")
else:
    print("ashish does not contain mundra")

# === operators


list1 = []
list2 = []
list3 = list1

# case 1
if (list1 == list2):
    print("True")
else:
    print("False")

# case 2
if (list1 is list2):
    print("True")
else:
    print("False")

# case 3
if (list1 is list3):
    print("True")
else:
    print("False")

# case 4
list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")


# Strings

# Assigning string to a variable
a = 'this is a string'
print(a)
b = 'this is a string'
print(b)
c = '''This is a string'''
print(c)
print("")

# list
l = [1,"a","string",1+2]
print (l)
l.append(5)
print (l)
l.pop()
print(l)
print("")

# Tuples in Python: A tuple is a sequence of immutable Python objects. Tuples are just like lists with the exception that tuples cannot be changed once declared. Tuples are usually faster than lists.
tup =(1,"a","string",1+2)
# print(tup)
print(tup[2])
print("")
# Iterations in Python: Iterations or looping can be performed in python by ‘for’ and ‘while’ loops. Apart from iterating upon a particular condition, we can also iterate on strings, lists, and tuples.
# loop condition
i = 1
while(i<10):
    print(i)
    i += 1
print("")

    # loop in string
s = "ashish mundra"
for i in s:
    print(i)
print("")

    # loop on list
l=[1,3,4,5,6,7,3,5]
for i in l:
    print(i)

print("")

# loop for range
for i in range (0,10):
        print(i)
print("")


# python string
# print a string
print("ashish mundra")
print("")
# Strings in Python
# SINGLE QUOTES
String1='welcome ashish mundra'
print(String1)
print("")

# DOUBLE QUOTES
String1="wELcome ashish mundra"
print(String1)
print("")

# TRIPLE QUOTES
String1='''welcome ashish mundra'''
print(String1)
print("")

# MULTIPLINE QUOTES
String1='''
          ashish
           mundra
           volyo 
           Solution'''
print(String1)
print("")
# characters of String
String1="Ashish mundra"
print("\n First  charcter  of string is:")
print(String1[0])
print("\n Second character of string is:")
print(String1[-2])
print("")
# reverse string python
aa = "ashishmundra"
print(aa[::-1])
print(aa[::-2])
# Program to reverse a string

gfg = "ashish"

# Reverse the strinh using reversed and join function
gfg = " ".join(reversed(gfg))

print(gfg)
print("")
# slicing
String1="ashish"
print(String1)
print("\nSlicing character from 1-6:")
print(String1[1:6])
print("\nSlicing character between"+"1st and 2nd last character:")
print(String1[1:-2])
print("")

# entrie string update
String1="Hello, i am ashish"
print(String1)
String1="ashish mundra"
print("\nUpdated String:")
print(String1)
print("")

# Escape Sequencing
String1='''i am ashish '''
print(String1)
String1 = "python\\ashish"
# print("\nEscaping Backslashes:")
print(String1)
String1 = "Hi \tashish"
print("\nTab:")
print(String1)
print("")
# list
list=[]
print("Blank list:")
print(list)
list=[10,20,30,40]
print("\nlist of number:")
print(list)
list = ["ashish","mundra"]
print("\nlist Items:")
print(list[0])
print(list[1])
print("")
# size of python
list1 = []
print(len(list1))
list2 = [10,29,80,69,75]
print(len(list2))
print("")
# input from python list
String = input("enter element (Space-Separated):")
lst = String.split()
print('the list is :',lst)

# insert()
list=[1,2,3,4]
print(list)
list.insert(3,11)
list.insert(0,'ashish')
print(list)
# extend()
list = [1,2,3,4]
print(list)
list.extend([8,'ashish','mundra'])
print(list)

# Reversing a list
mylist = [1,2,3,4,5,'ashish','mundra']
mylist.reverse()
print(mylist)
# remove()
list=[1,2,3,4,5,6,7,8,0,]
print(list)
for i in range(1, 5):
    list.remove(i)
# list.remove(5)
# list.remove(6)
print(list)
print("")
# pop()
list = [1,2,3,4,5]
list.pop()
print(list)
list.pop(2)
print(list)
list.pop(2)
print(list)
print("")

# tuple
Tuple1 = tuple("ashish")
print(Tuple1[0])
Tuple1 = ("ashish","mundra")
a , b  = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print("")

Tuple1= (0 , 1 , 2 , 3)
Tuple2=('ashish','mundra')
Tuple3 = Tuple1+Tuple2
print("Tuple1:")
print(Tuple1)
print("\nTuple2:")
print(Tuple2)
print("")
print(Tuple3)
print("")
# # Deleting
# Tuple1 = (0, 1, 2, 3, 4)
# del Tuple1
#
# print(Tuple1)

# set
my_set = {1, 2, 3}

print(my_set)
print("")
set1 = set([4,5,(6,7)])
set1.update([9,4])
print("\n")
print(set1)
print("")
set1= set([1,2,3,4,5])
# print("\n")
print(set1)
set1.clear()
# print("/n")
print(set1)
print("")
# python array
a=arr.array('i',[1,2,3])
print("the new created array is :",end=" ")
for i in range(0,3):
    print(a[i],end= " ")
print()

b= arr.array('d',[2.5,3.2,3.3])
print("the new created array  is :",end=" ")
for i in range (0,3):
    print(b[i],end=" ")
print("")
# removing a array

arr= array.array('i',[1 , 2,3,4,5])
print("created new array is:",end="")
for i in range (0,5):
    print(arr[i], end=" ")
print("\r")
print("the popped element  is :",end="")
print(arr.pop(2))
print("the array after popping is :",end="")
for i in range (0,4):
    print(arr[i],end=" ")
print("\r")
arr.remove(1)
print("the array after removing is :",end="")
for i in range (0,3):
 print(arr[i],end =" ")
print("")


# slicing as array
l=[1,2,3,4,5,6,7,8,9 ,10]
a=array.array('i',l)
for i in (a):
 print (i, end=" ")
Sliced_array =a[3:8]
print(Sliced_array)
Sliced_array=a[5:]
print(Sliced_array)
Sliced_array=a[:]
print(Sliced_array)
print("")


# updating array
arr=array.array('i',[1,4,5,7,3,4,5])
print("array before updation:",end="")
for i in range (0,7 ):
    print (arr[i],end=" ")
print("\r")
arr[2] = 5
print("array after  updation :",end=" ")
for i in range (0,7 ):
    print (arr[i],end=" ")
print()
arr[6] = 2
print("array after  updation :",end=" ")
for i in range (0,7 ):
    print (arr[i],end=" ")
print()
print("")

# control flow
# if statement

i=10
if(i>15):
    print("10 is less than 15")
print("i am not in if")
print("")
# if else
i=20
if(i<15):
    print("i is smaller than 15")
    print("i'm in if block")
else:
    print("i is greater than 15")
    print("i am in else block")
print("i'  m not in if and not in else block")
print("")
# nested if
i=10
if(i==10):
   if(i<15):
       print("i is smaller than 15")
if(i<12):
    print("i is samller than 12 too")
else:
    print("i is greater than 15")
print("")

# if-elif-else
# if (condition):
#     statement
# elif (condition):
#     statement
# .
# .
# else:
#     statement
i=20;
if(i==10):
    print("i is 10")
elif(i == 15):
    print("i is 15")
elif(i == 20):
    print("i is 20")
else:
    print("i is not present")
print("")
# Short Hand if statement
i =10
if i <15:
    print("i is less than 15")
print("")
# Short Hand if-else statement
i=10
print(True) if i<15 else print (False)
print("")

# loops
l=["ashish","mundra"]
for i  in l:
    print(i)
print("")
# Loops in Python String
s="ashish"
for i in s:
    print(i)
print("")

# Loop Control Statements
# Continue Statement in Python
for letter in 'ashishmundra':
    if letter == 'i':
        continue
    print('current letter:', letter)
print("")
# Loop with Break Statement
for letter in 'ashishmundra':
    if letter == 'm' or letter == 'i':
       break
    print('current letter:',letter)
print("")
# loop with range function
for i in range(10):
    print(i,end=" ")
sum=0
for i in range (1,10):
    sum= sum+i
    print("\nSum of first 10 number:",sum)
print("")
# loop in Python with else
for i in range (1,10):
    print(i)
else:
    print("no break\n")
print("")

# Python While Loop
count=0
while(count<1):
    count= count+1
    print("hello ashish")
print("")
# loop with list
a=[1,2,3,4,5]
while a:
    print(a.pop())
  # Whileloop with else
i=0
while i<4:
    i += 1
    print(i)
    break
else:
 print("no break")
print("")
# break
num=0
for i in range(10):
       num += 1
       if num == 8:
            break
       print("the num has value:",num)
print("out of loop")
print("")

# continue statement
for var in "ashishmundra":
    if var == "e":
        continue
    print(var)
print("")

# range
for i in range (1,11):
    if i == 6:
        continue
else:
    print(i, end =" ")
print("")
 # pass

li = ['a', 'b', 'c', 'd']

for i in li:
    if (i == 'a'):
        pass
    else:
        print(i)