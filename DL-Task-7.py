#Defining Function
def greet():
    """Display a simple greeting Message"""
    print("Hello! How are you ?")

greet() #function call

#Defining Function with one argument 
def greet(name):
    print("Hello! "+ name.title() +" How are you?")
greet('Faiz')

#TRY IT YOURSELF 8-1
def display_message():

    """Displaying what I am learning"""
    print("I am learning Functions in Python")
display_message()

#TRY IT YOURSLF 8-2
def fav_book(name):
    """"Displaying Fav book name"""
    print(name +" book is Wonderland")
fav_book('Alice')

#Passing Argumments
def info(name, age):
    print("My name is "+ name)
    print (name + " is "+ str(age )+ "years old.")
info('Faiz',22)

#calling multiple Functions
print("\nCalling multiple function")
def info(name, age):
    print("My name is "+ name)
    print (name + " is "+ str(age )+ "years old.")
info('Anna',26)
info('Salar', 23)

#Return Values
def city_country(city, country):
    message='"' +city +", "+country+'".'
    return message #returning values
full_message= city_country('Swat', 'Pakistan')
print(full_message)

#Arbitary Numbers of Arguments
def fav_book(*name):
    """"Displaying Fav book name"""
    print(name )
fav_book('Alice')
fav_book('anna','salar', 'huma','sam')

#Method 2
def fav_book(*name):
    """"Displaying Fav book name"""
    for names in name:
        print(names.title() +" book is Wonderland")
fav_book('Alice')
fav_book('anna','salar', 'huma','sam')

#add function
def add(a,b):
    print("Sum of a and b is : " ,a+b)
add(10, 20)

#using arbitary arguments keyswords
def user_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""
 profile = {}
 profile['first_name'] = first
 profile['last_name'] = last
 for key, value in user_info.items():
    profile[key] = value
    return profile
info = user_profile('albert', 'einstein',
 location='princeton',field='physics')

print(info)
