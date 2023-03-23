#Working With Dictionaries

x={1: 'python',2: 'cpp', 3:'HTML'}
print(x[1])
print(x[3])
print(x[2])

#Adding New Key Value Dictionary
x[4]='JavaScript'
x[5]='CSS'
print(x)

#Adding key values in empty list
a={}
a['x']='abc'
a['y']='def'
a['z']='ghi'
a['m']='jkl'
print("\n",a)

#Modifying key value in Dictionary
a['x']='ABC'
a['y']='DEF'
a['z']='GHI'
a['m']='JKL'
print("\n",a)

#Removing Key VAlue Dictionary
print("\n",x)
del x[5]
del x[2]
print(x)

print("My favorite Language is" ,x[1].title())

#Dictionary Methods
print("\nKeys() : ",a.keys())
print("\nvalues() :",a.values())
print("\nitems() :", x.items())
print("\nGetting value for pyhton using get() :",x.get(1))
print("\nPopping HTML from dictionary: ",x.pop(3),"\nAfter Popping HTML: ", x)
print("\nPopitem() :" ,a.popitem())
print("\nValues :" ,a.values())
print("\nUpdate() :", a.update({'a' :'MNO'}), "After Updating : ", a)


#Try it Yourself 6-1
Info={'Name' : 'Faiz', 'age': 22 , 'city':'Islamabad' }
print("Name :" +Info['Name'])
print("Age :"+str(Info['age']))
print("City :"+Info['city'])

#Try it Youself 6-2
names={ 'Zainab': 2, 'Anna':6, 'Sana':7}

for name , number in names.items():
    print(name+"'s" +" Favorite Number is "+str(number)) 

#try it yourself 6-3
programming_words={'list': "Lists are used to store multiple items in a single variable.",
                'loops':"Lopp is used to iterate over a sequence ",
                'sets':"Set is one of 4 built-in data types in Python used to store collections of data"}

for word, words in programming_words.items():
    print("\n" + word +" :\n"+words)



