print("\t\t\tINSERTING ELEMENTS IN LIST\n")
program=['Javascript','C/C++']
program.insert(0, 'Python')
program.insert(2, 'HTML')
program.insert(1, "Java")
program.insert(4, "CSS")
print(program)

print("\n\t\t\t DELETING ELEMENT FROM LIST USING Del METHOD\n")
print(program)
del program[1]
del program[-1]
print("\n\t\t\tAfter Deleting Elemtss from list\n")
print(program)

print("\n\t\t\t DELETING ELEMENT FROM LIST USING pop() METHOD\n")
print(program)
print("\n\t\t\tAfter Deleting Elemtss from list\n")
program.pop()
program.pop(-2)
print(program)
message= "I am learing "+ program.pop(0)
print(message)

print("\n\t\t\t REMOVING ITEM BY VALUE\n")
program.insert(1, 'C#')
print(program)
program.remove('C#')
print(program)
a='Python'
print("I am learning "+ a)

print("\t\t Initializing List\t\t")
objects=['pen', 'pencil' ,'notebook','bottle']
print(objects)
print("'\n\t\tAccssing elements in list\t\t")
print(objects[0])
print("\n\t\tPrinting element of list in formatted form\t\t")
print(objects[1].title())
print("\n\t\tAccessing -1 elements of list\t\t")
print(objects[-1])
print("\n\t\tAccessing -3 elements of list\t\t")
print(objects[-3])
print("\n\t\tUsing individual value from list and printing a message\t")
message= "I don't have a " + objects[0]
print(message)

print("\t\t Initializing List\t\t")
objects=['pen', 'pencil' ,'notebook','bottle']
print(objects)
print("'\n\t\tAccssing elements in list\t\t")
print(objects[0])
print("\n\t\tPrinting element of list in formatted form\t\t")
print(objects[1].title())
print("\n\t\tAccessing -1 elements of list\t\t")
print(objects[-1])
print("\n\t\tAccessing -3 elements of list\t\t")
print(objects[-3])
print("\n\t\tUsing individual value from list and printing a message\t")
message= "I don't have a " + objects[0]
print(message)
print("\t\t\t MODIFYING ELEMENT IN LIST")
names=['Hira','Muskan','Ali','Sara']
print(names)
print("\t\t\t After Modifying Ali")
names[2]='Faiza'
print(names)

print("\t\t\t ADDING ELEMENT IN LIST")#use .append() to add a new element
print(names)
names.append('Aiza')
print("\t\t\t After Adding a New Element")
print(names)



print("\n\t\t\t Permanently Sorting\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print("\n\t\t\t Printing above list in Reverse Order\n")
cars.sort(reverse=True)
print(cars)

print("\n\t\t\t Temporary Sorting\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

print("\n\t\t\tPrinting List in Reverse Order\n")
cars.reverse()
print(cars)

print("\n\t\t\tFinding Length of List\n")
print(len(cars))
for a in range(0,5):
    print(a)
a= list(range(1,6))
print (a)

print(min(a))
print(max(a))
print(sum(a))

guest_list=['Anna','Sam', 'karl', 'Rida']
print(guest_list[0:2])
print ("\nLopping through a Slice ")
print("\nHere are the first three players on my team:")
for guest in guest_list[:3]:
 print(guest)


friend_guest = guest[:]
print("My favorite guest are:")
print(guest)
print("\nMy friend's fav guest are:")
print(friend_guest)

print("\t\t\tTry It Yourself 3-1")
friends_names=['zainab','nida','ayesha','maryam','noor']
print("First Element: ",friends_names[0].title())
print("Second Element: ",friends_names[1].title())
print("Third Element: ",friends_names[2].title())
print("Fourth Element: ",friends_names[3].title())
print("Fifth Element: ",friends_names[4].title())

print("\t\t\tTry It Yourself 3-2")
message='Hi ' +friends_names[0].title() + '! How are you?'
print(message)
message='Hi ' +friends_names[1].title() + '! How are you?'
print(message)
message='Hi ' +friends_names[2].title() + '! How are you?'
print(message)
message='Hi ' +friends_names[3].title() + '! How are you?'
print(message)
message='Hi ' +friends_names[4].title() + '! How are you?'
print(message)

print("\t\t\tTry It Yourself 3-3")
train=['Golden Arrow','Blue Train','Bullet Train','TGV','Orient Express']
message ='I would like to own '+ train[2]
print (message)
message=train[0]+ ' is the fastest train in world'
print(message)
message= train[-1] +' is a great public carrier '
print(message)
message=train[-2] +' stands for Train à grande vitesse'
print(message)
print("\t\t\tTry  It Yourself 1 Completed\n")
print("\n\t\t\tTry It Yourself 3-4")
guest_list=['Anna','Sam', 'karl', 'Rida']
print(guest_list)
print(guest_list[0]+"! would you like to join us on dinner today?")
print(guest_list[1]+"! would you like to join us on dinner today?")
print(guest_list[2]+"! would you like to join us on dinner today?")
print(guest_list[3]+"! would you like to join us on dinner today?")

print("\n\t\t\tTry It Yourself 3-5\n")
print("Its OK" + guest_list[2]+"if you can't join us today.")
guest_list[2]='sara'
print(guest_list[2]+"! would you like to join us on dinner today?")
print("\n Karl wasn't able to join us today for Dinner")

print("\n\t\t\tTry It Yourself 3-6\n")
print(guest_list)
guest_list.insert(0, 'Aima')
guest_list.insert(-1, 'Zarnish')
guest_list.append('Hina')
print(guest_list)

print("\n\t\t\tTry It Yourself 3-7\n")
message="I apologize I can't invite you to dinner"
#guest_list.pop()
print(guest_list.pop()+"!" +message)
print(guest_list.pop()+"!" +message)
print(guest_list.pop()+"!" +message)
print(guest_list.pop()+"!" +message)
c=guest_list.pop(0)
print(c+"! "+message)
print(guest_list)
message=" You are still invited!"
print(guest_list.pop() + message)
print(guest_list.pop() +message)
print("\t\t\tTry It Yourself 3-8")
loc=['Germany','Switzerland','America','turkey','Canada']
print("\n Original Order")
print(loc)
print("\n Sorted list")
st=sorted(loc)
print(st)
print("\n Original Order")
print(loc)
print("\n Reversing List")
print(loc.sort(reverse=True))
print(loc.reverse())
print("\n Original Order")
print(loc)
print("\n Using Sort")
loc.sort()
print(loc)

print("\t\t\tTry It Yourself 3-9")
guest_list=['Anna','Sam', 'karl', 'Rida']
print("\n Printing Length")
print(len(guest_list))
print("\n\t\t\tTry It Yourself 4-1")
fav_pizzas = ["Pepperoni", "Margherita", "BBQ"]
for pizza in fav_pizzas:
    print(pizza)

print("\n")

for pizza in fav_pizzas:
    print("I like"+ pizza+" pizza")
print("\nPizza is my Fav food")

print("\n\t\t\tTry It Yourself 4-2")

animals=['dog','cat','Parrot']
for aml in animals:
    print(aml)
print("\n")

for aml in animals:
    print(aml+ " would make a great pet\n")

print("All the above animals would make great pet")

print("\t\t\tTry It Yourself 4-3")
for a in range(1,21):
    print(a)


print("\t\t\tTry It Yourself 4-5")
for a in range(1,21,2):
    print(a)

print("\t\t\tTry It Yourself 4-6")
mul =[number for number in range(3,21,3)]
for number in mul:
    print(a)

print("\t\t\tTry It Yourself 4-7")
cube=[number**3 for number in range(1,11)]
for cube in cube:
    print(cube)

print("\t\t\tTry It Yourself 4-8")
cube =[number**3 for number in range((1,11))]
print(cube)
menu = ('rice', 'chicken', 'salad', 'bread', 'tea')
for food in menu:
    print(food)
menu = ('chowmin', 'beef', 'salad', 'garlic bread', 'soup')
for food in menu:
    print(food)
menu[0] = 'pasta'
for food in menu:
    print(food)
    