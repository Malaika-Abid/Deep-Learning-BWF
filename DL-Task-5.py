#User input
name = input("Enter you  name: ")
print("Welcome "+name)

#input() in python
a= input("Enter first number: ")
b=input("Enter second number: ")
print("first number you enter is:", a)
print("second number you enter is:",b)

x=int(input("\nenter 1st number: "))
y=int (input("\nenter 2nd number: "))
print(x)
print(y)

x=int(input())
y=int(input())
message =(" Numbers you entered are :")
print(message ,x,"and",y)

#TRY IT YOURSELF
#: Write a program that asks the user what kind of rental car they 
#would like. Print a message about that car, such as “Let me see if I can find you 
#a Subaru.
car= input("\nWhat kind of rental car you want? ")
print("Let me see if  can find you a ", car)

#Write a program that asks the user how many people 
#are in their dinner group. If the answer is more than eight, print a 
#message saying they’ll have to wait for a table. Otherwise, report that
#their table is ready.
grp= int(input("\nHow many people are thier in your dinner group? \n"))
if (grp > 8):
    print("Sorry! You have to wait for table")
else:
    print("Table is ready")

#Ask the user for a number, and then report whether the 
#number is a multiple of 10 or not

num= int(input("\nEnter a Number"))
if (num%10)==0:
    print("The number is multiple of 10")
else:
    print("The number is not multiple of 10")

#enumerate()

# Python program to illustrate
# enumerate function
guests=['Sara','Ali','Huma','Salar']
print(list(enumerate(guests)))

#enumerate in tuple
flowers =[(1,'peruvian'),( 2,'lily'),(3,'lotus'), (4,'daisy')]
for i , j in enumerate(flowers):
    print(i,j)
    

string1="Malaika"
str1=list(enumerate(string1))
print(str1)

a= input("\nEnter you Name and I will count letters in it: ")
print(list(enumerate(a,1)))

#CONDITIONAL
#Tests for equality and inequality with strings
name="Maryam"

if name!='Teufel':
    print((name=='Maryam'))

if name=='Maryam':
    print(name=='huma')

#Tests using the lower() function
name = 'AyeShA' 
print(name.lower()=='ayesha')

name=input("\nEnter Name: ")
name2=input("\nEnter Name: ")
if name==name2:
    print(name.lower()==name2)
    print(name)
else:
    print(name==name2)

#Numerical tests involving equality and inequality, greater than and 
#less than, greater than or equal to, and less than or equal to

a=10
b=20
if a==b:
    print("\na & b are equal")
if a!=b:
    print("\na & b are not equal ")
if a>b:
    print("\na is greater than b")
if a<b:
    print("\na  is less than b ")
if a>=b:
    print("\na is greater or equal to b")
if a<=b:
    print("\na is less or equal to b")

#Tests using the and keyword and the or keyword
a=5
b=10
c=15
if a>b and a>c:
    print("\na is greater ")
if b>a or b>c:
    print("\nb might be greater ")

#Test whether an item is in a list    

objects=['cellphone','pen','bottle']
object2=[1,4,6,7,4,3]
if 'cellphone' in objects:
    print("\ncell phone is present in your list")
else:
    print("\ncellphoneis not present in your phone")
if 9 in object2:
    print("9 is in your list ")
else:
    print(" 9 is not in your list")

#SETS
a= {1, 4,5 ,67,7}
print(type(a))

my_set={1,2,3,3,4,6,5,4,3}
print(my_set)

#my_set[2]= 9 (set doesn't support item assignment)

my_set.add(12)
print(my_set)

#Normal VS Frozen Set
print("\nNormal set: ")
normal={1,'oop',6.5,3,6,9.8,'cpu'}
print(normal)

print("\nFrozen Set: ")
frozen= frozenset({ 1,'Or',54,'Nope','bye'})
print(frozen)

#frozen.add('hello') #frozenset have no attribute 'add'

#SET UNION

num1={1, 2 ,4 , 6 , 7,10} 
num2={0,5,3,2,1}
set_union=num1.union(num2)
print("\nUnion of Num1 and Num2: ",set_union)
#Union using '|'
set_union=num1 | num2
print("\nUnion of Num1 and Num2 using '|' : ",set_union)


#SET INTERSECTION
num1={1, 2 ,4 , 6 , 7,10} 
num2={0,5,3,2,1,6,10,11,1}
set_intersection= num1.intersection(num2)
print("\nIntersection of Num1 and Num2: ",set_intersection)
#Intersection using '&' operator
set_intersection=num1 & num2
print("\nIntersection of Num1 and Num2 using '&' : ",set_intersection)

 
#Set Symmetric Difference (union)
flowers={ 'rose', 'tulip','Sunflower','lily'}
flowers2={'orchid', 'tulip','Dandelions','daisy'}
flowers3 ={'peruvian lily','lotus', 'daisy'}

sym_diff=flowers.symmetric_difference(flowers2)
print("\nSymmetic difference flowers and flowers2 : ",sym_diff,"\n")

print("\nSymmetric Difference of all flowers set :", flowers^flowers2^flowers3)

#Set difference (intersection)
flowers={ 'rose', 'tulip','Sunflower','lily'}
flowers2={'orchid', 'tulip','Dandelions','daisy'}
flowers3 ={'peruvian lily','lotus', 'daisy'}
 
set_diff=flowers.difference(flowers2)
print("\nSet difference :", set_diff)

#Time Your Code
import time
start= time.time()

flowers1 =['lily','lotus', 'daisy']
print(list(enumerate(flowers1)))
    
print("time taken by list :", start)
start2=time.time()

flowers2 =[(1,'peruvian'),( 2,'lily'),(3,'lotus'), (4,'daisy')]
for i , j in enumerate(flowers2):
    print(i,j)
print("Time taken by tuple: " ,start2)

