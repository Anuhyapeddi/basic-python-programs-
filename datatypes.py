#introduction to data_types in python 
""" Number are represented in 3 types 
     1. Integer 
           " Integer is divied into 2 types they are   
                    a. boolean 
                    b. Long int "
     2. Float
     3. Complex  """ 

# integer
a = 1 
b = 4
d = a+ b
print(d)
type(d)

# long int 
a = 2*1000000
print(a)
type(a)

#boolean (returns True or False value)
a = 1
print(bool(a))
type(a)

# float  
a = 4.5
print(a)

#complex
a = 3+4j
print(a)
type(a)
print(imag(a)) # displays the real part of a
print(real(a)) # displays the img part of a

#string 
a = "Happy to see you, this is Anuhya Shetty"
print(a)
type(a)

#list(A single list can contain strings, integers, as well as objects, lists are mutable, represented in square bracket)
list1 = [1, "a", "anuhya", 1+8]
print(list1)
type(list1)

#tuple(Tuple is also used to store data/values, tuples are immutable, represented in round bracket)
tup = (1, "a", "chinnu")
print(tup)
type(tup)

#dictionary(stores both Key and Value, represented by curly brackets)
dict = {1 : "apple", 2 : "banana", 3 : "candy", 4 : "dominos pizza"}
print(dict)
type(dict)

#set(The elements in the set are not repeated)
s = set("Python is lub ")
print(s)
type(s)

