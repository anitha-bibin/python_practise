#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:46:04 2021

@author: anitha
"""

"""
---------------------------------------------------------------

1. Write a Python program which accepts the radius of a circle from 
the user and compute the area.
---------------------------------------------------------------
"""
#%%

rad=int(input("enter the radius of the circle\n"))

print("area of the circle =",3.17*(rad**2))

 #%%
""" 
---------------------------------------------------------------

2. Write a Python Program to accept the details of a student like name, roll
number and mark and display it.
Sample input: Enter the name: Anisha
Enter the roll number: 21
Enter the mark: 78
---------------
"""
#%%

stu_name=str(input("Enter student's name\n"))
stu_roll=int(input("Enter the students roll no\n"))
stu_mar=int(input("Enter the mark\n"))

print("name:",stu_name,"\n ")
print("roll number:",stu_roll,"\n ")
print("mark:",stu_mar,"\n ")

    #%%
""" 
---------------------------------------------------------------
3. Write a Python program to get the largest number from a list.
-------------
"""
#%%

nums=[12, 3, 147, 10,98,223,34]
print(max(nums))



    #%%
""" 
---------------------------------------------------------------

4. Write a Python program to accept a string value from the user and display
the count of each character in that string.
---------------
"""
#%%
newstr=str(input('enter a string')).strip()
new_word=[]
for i in newstr:
    if i not in new_word:
        new_word.append(i)
        print(i,"occured ",newstr.count(i),"times")
    
    #%%
"""   
---------------------------------------------------------------
5. Write a Python program to copy element 44 and 55 from the following tuple
into a new tuple.
-------------
"""
#%%
 
tuple1 = (11, 22, 33, 44, 55, 66)

tuple2=(51,32,21,45,24,63)

finaltuple=tuple2[:4]+(44,55)

print(finaltuple)


tolist=list(tuple1)
tolist[3]=88
tolist[4]=99
totuple=tuple(tolist)
print(totuple)
    #%%
""" 

----------------------------------------------------------------------
6. Given a range of first 10 numbers, write a Python program to iterate from
start number to the end number and print the sum of the current number
and previous number.
----------
"""
#%%

for i in range(1,11):
    print("curr num: ",i," prev num: ",i-1," and total is ",i+(i-1),"\n")
   
    #%%
"""    
----------------------------------------------------------------------
7. Write a Python program to print only those numbers which are divisible of 5.
"""
#%%

num_list=[15,21,32,35,47,49,55,65,20]

for i in num_list:
    if(i%5==0):
        print(i)
        #%%
""" 
----------------------------------------------------------------------------
8. Write a Python program to check whether a number is prime or not.

"""
#%%
check_num=int(input("enter a number"))
for i in range(2,check_num):
    if(check_num%i==0):
            print(check_num," not a prime number")
            break
else:
    print(check_num," is a prime number")
 
    #%%
""" 
----------------------------------------------------------------------------
 
 9. Write a Python program to reverse a list using for loop.
"""
 #%%
 
reverse_list=[12,81,62,45,73,32]
print(reverse_list.reverse())

new_list=[]
j=0
for i in reverse_list:
    new_list.insert(j,i)
    j=j+1
print("here",new_list)   
  

    #%%
""" 

----------------------------------------------------------------------------
10. Write a Python program to print the following pattern.
*
**
***
****

"""
#%%           
pattern_ct=int(input("enter count less than 10"))
if(pattern_ct<=10):
    for i in range(1,pattern_ct+1):
        print(i*"*")
else:
    print("entera number less than 10")     
    
    #%%
"""   
 ----------------------------------------------------------------------------   
11. Write a Python function to find the maximum of three numbers

"""
#%%
    
sample=[]
sample.insert(0,int(input("enter first number")))
sample.insert(1,int(input("enter second number")))
sample.insert(2,int(input("enter third number")))
sample.sort()
print(sample[-1]," is the biggest number")

#%%
"""
---------------------------------------------------------------------------
12. Write a Python function called exponent(base,exp) that returns an integer
value of base raises to the power of exp.
"""
#%%


def power_of(ba,exp):
        power_value=ba**exp
        return power_value
        

ba=int(input("enter base value"))
exp=int(input("enter exponent value"))
print("the answer is ",power_of(ba,exp))
#%%
"""

----------------------------------------------------------------------------
13. Write a Python function that takes a positive integer and returns the sum of
the cube of all the positive integers smaller than the specified number.
Sample input: 4
Sample output: 36
"""
#%%
def cube_of(num):
    sum=0
    for i in range(1,num):
        sum=sum+i**3
    return sum    
        

val1=int(input("Enter a number"))
print("the sum of cubes of all the numbers below ",val1," is",cube_of(val1)) 

#%%    
"""   
----------------------------------------------------------------------------

14. Write a Python program to construct the following pattern, using a nested
for loop.
*
**
***
****
*****
****
***
**
*
"""
#%%
val1=int(input("Enter a number"))
j=0

def print_st(num):
    print(num*"*")
    

for i in range(1,3):
   for j in range(1,val1+1):
       if(i==2):
           pstar=val1-j
           print_st(pstar)
       else:
           print_st(j)
#%%
"""
----------------------------------------------------------------------------
15. Write a Python program which iterates from 1 to 10. For multiples of 2,
 print “Fizz” instead of the number and for the multiples of 5, print “Buzz”. 
 For numbers which are multiples of both 2 and 5, print “FizzBuzz”.
"""

#%%
for i in range(1,11):
    if(i%2==0 and i%5==0):
        print("fizzBuzz")
    elif(i%2==0):
        print("fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
        
#%%
"""    
 ----------------------------------------------------------------------------
 16. Write a Python program to find the most frequent item in a list of numbers.
Sample input: 2, 3, 4, 2, 5, 2
Sample output: 2

"""
 #%%

num_list=[14,3,18,25,3,21,52,18,62,32,24,22,22]
new_list={} #dictionary created
for i in num_list:
    item_len=num_list.count(i)
    if(item_len>1 and i not in new_list.keys()):
       new_list[i]=item_len #more occured elements are added to dict
       
print(new_list)
k=list(new_list.keys()) # get the list of keys
v=list(new_list.values()) #get the list of values
print(k[v.index(max(v))]) #get the key whos value is max of value

 #%%
"""
---------------------------------------------------------------------------
 17. Write a Python program to find the sum of squares of the numbers
 in a list.
 Sample input: 2,1,3,1
Sample output: 15
 
 """
 #%%
num_list=[2,1,3,1]
sum=0
for i in num_list:
     sum=sum+i**2

print(sum)     
     
 #%%
"""
-----------------------------------------------------------------------------

   18. Write a Python program using for loop that will iterate from 1 to 15.
   For each iteration, check if the current number is odd or even, and display the
message to the screen as odd or even.
Sample input: 1....15
Sample output: 1-odd
2-even
....
15-odd

"""
#%%


for i in range(1,16):
    if(i%2==0):
        print(i, "-even")
    else:
        print(i,"-odd")
#%%
"""
19. Write a Python program to convert temperatures to and from Celsius
Fahrenheit. [Formula: c/5=f-32/9 where c=temperature in Celsius and f=
temperature in Fahrenheit.]
Sample input: Temperature in Fahrenheit =41
Sample output: Temperature in Celsius =5

"""
#%%
temp=int(input("enter temperature"))
unit=input("enter unit C or F").upper()
if(unit=='C'):
    to_fahren=temp*(9/5) + 32 
    print("TEMPERATURE IN FAHRENHEIT IS ",to_fahren)
elif(unit=='F'):
    to_celsius=(temp-32)*5/9
    print("TEMPERATURE IN CELSIUS IS ",to_celsius)
else:
    print("invalid unit")    
        
#%%

"""
20. Write a Python function to calculate the factorial of a number (a non-
negative integer).The function accepts the number as an argument.
Sample input: 3
Sample output: 6
"""
#%%
val1=int(input("Enter a number"))
sum=1
for i in range(1,val1+1):
    sum=sum*i
print(sum)

#%%

#%%
L = [1,3,4,5,6,7,8,9,10,12,15,20,21,22] 
print(L[2:5:2])


print(*L) # prints the list without coma

print(*L,sep=":")

print("MOUSSE"!="MOUSSE") #  != operation is done

d={0:"a",1:'b',2:"c",3:"d"}
for i in d:
    print(d[i])
    
    

#%%

#%%

val1=int(input("Enter  number  elements"))
sum=1
for i in range(0,val1):
    newlist.insert(i,int(input()))

print
#%%









