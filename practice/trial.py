x = ('masala', 'lemon', 'ginger') #making tuple
y = enumerate(x) #enumerating the tuple. it returns an enumerate object.
print(y)    
print(list(y)) #converting the enumerate object to a list. it returns a list of tuples. each tuple contains the index and the value of the tuple.
d = {
    1:"iron-man",
    2:"spider",
    3:"batman",
}
print(d) #printing the dictionary
print(list(d))
f = open("test.py") #opening the file in read mode in memory and taking its refernce in f.
a = open("hello.py", "w") #opening the file in write mode in memory and taking its refernce in f.if file does not exists, it creates a new file.
# we can use try and catch syntax to read a file.

# try:
#     a.write("print('hello world')") #writing to the file
# finally:
#     a.close() unloading the file from memory
# #closing the file


# new syntax to open a file
with open("hello.py", "w") as a:
    a.write("print('hello jatin')") #writing to the file
# with statement automatically closes the file after the block of code is executed