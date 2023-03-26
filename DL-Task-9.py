#File Handling and Exceptions
# Know your Path
import os 
print(os.getcwd())

#Reading entire File(Method-1)
with open('read_file.txt') as file_object:
    contents=file_object.read()
    print(contents)

#Reading entire File(Method-2)
filename= 'python.txt'
with open(filename) as file_object:
    contents=file_object.read()    
    print("\n",contents)

#making a list of lines in Python
with open(filename) as file_object:
    lines= file_object.readlines()

for line in lines:
    print("\n",line.strip())

#Working with File Content
with open(filename) as file_object:
    lines= file_object.readlines()

str1=''
for line in lines:
    str1+=line
print(str1)
print("\n",len(str1))

#TRY It YOURSELF 10-1
filename2='Learning_Python.txt'
with open(filename2) as file_object:
    contents= file_object.read()
print(contents.strip())

#looping over file object and printing each line in learing _Pyhthon.txt 
with open(filename2) as file_object:
        for line in file_object:
            print(line)

with open(filename2) as file_object:
    lines= file_object.readlines()

for line in lines:
    print(line)

#TRY IT YOURSELF 10-2

for line in lines:
    update_line= line.replace('Python','C')
    print(update_line)

#Writing to empty file
with open('writing.txt','w') as file_object:
    file_object.write("I am Malaika and I am learning Files in Python. GoodBye!")
    file_object.write("\nPython is easy as compare to C++.")

# appending in 'read_file.txt'
with open('read_file.txt','a') as file_object:
    file_object.write("\nI am appending in files.")

#TRY IT YOURSELF
a= input("Enter you name:")
with open('guest.txt', 'w') as file_object:
   filee= file_object.write(a)
print("Name you entered is :", a)

#TRY IT YOURSELF
while True:
    name=input("Enter your name , or press q to quit.")
    if name=='q':
        break

with open('guest-book.txt','a') as file_object:
        file_object.write(name)

message="Welcome! "+ name
print(message)

#Try - except 
try:
    print(9/0)
except: 
    print("You can't divide by zero.")

#TRY IT YOURSELF
while True:

    try:
        a= int(input("Enter 1st number: "))
        b= int(input("Enter 2nd number: "))
        answer = a + b
    except: 
        print("Enter  Valid Numbers ")
    else:
        print(answer)
        break
#TRY IT YOURSELF 
filenames=['cat.txt','dog.txt']
for filename in filenames:
    try:
        with open(filename) as file_object:
            contents=file_object.read()
            print(contents)
    except:
        print(filename+" not found")

filename='Programming poll.txt'
while True:
    reason= input("why do yu like programming, type 'q' to quit.")
    if reason=='q':
        break
    else:
        with open(filename,'a') as file_object:
            filei =file_object.write(reason)












