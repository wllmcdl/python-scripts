#### Swaping Values
```python
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
    
fib(1000)
```

In ```a, b = b, a + b``` the expressions on the right hand side are evaluated before being assigned to the left hand side. So it is equivalent to:

```python
tmp = a + b
a = b
b = c
```

#### String format f
```python
age = 33
name = 'John
x = f"My name is {name} and I'm {age} years old"
```
#### Ternary
If condition is ```True``` than ```x = 1``` else ```x = 0```
```python
x = 1 if condition else 0 
```
#### Large Numbers
In python this ```1000000000``` is equals to this ```1_000_000_000``` to make it easy on the eyes
we can even format the output:
```python
x = 1_000_000_000
print(f'{x:,}')
```
the result will be ```1,000,000,000```

#### File Stream
We use ```with``` when we're setting up and tearing down resources, in this case it will automatically close down the file  
```python
with open('text.txt', 'r') as myFile:
    fileContents = myFile.read()
```

#### Lists
- ##### enumerate
```python
names = ['John', 'Charles', 'Wolverine']
surnames = ['Cena', 'Xavier', 'Delgado']
ages = [73, 69, 56]

# The start=1 is for printing purposes, so it start at one. The default is 0
for index, name in enumerate(names, start=1):
    print(f'My name is {index}, name')

Results
(1, 'John')
(2, 'Charles')
(3, 'Wolverine')
```
- ##### zip
```python
for name, surname, age in zip(names, surnames, ages):
    print(f"My name is {name} {surname}, and I'm {age} years old.")
    
Results
My name is John Cena, and I'm 73 years old.
My name is Charles Xavier, and I'm 69 years old.
My name is Wolverine Delgado, and I'm 56 years old.
>>>
```

#### Unpacking
```python
In
a, b, *c = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)

Out
1
2
[3, 4, 5]
```
```python
'''' if we want to ignore a value we put an _ (underscore) in its place and many values we put *_ (means the rest of the values)'''

a, b, _, d, e = (1, 2, 3, 4, 5)

print(a)
print(b)
print(d)
print(e)

Out
1
2
4
5
```
```python
In
a, b, c, *_ = (1, 2, 3, 4, 5, 6, 7)

print(a)
print(b)
print(c)

Out
1
2
3
```

```python
a, *b, c, d = (1, 2, 3, 4, 5, 6)

print(a)
print(b)
print(c)
print(d)

Out
1
[2, 3, 4]
5
6
```

#### getting and setting attributes with setattr and getattr built-in functions

```python
class Python:
    pass
    
person = Person()

#we can set attributes automatically on python, like this
person.name = 'William'
person.age = 33

#the result would be 'Wiliam'
print(person.name) 

#But in this case we want to set attributes via a variable
key = 'surname'
value = 'Lopes'

#It can't be this way because then our attribute name would be var1
person.var1 = var1 

#We can make use of a builtin function named setattr
setattr(person, key, value)

print(person.surname) #will print Lopes
```
```python
#a particular case it might be useful is this:

person_info = {'name':'jorge','age':'56'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

Out
jorge
56
```
#### Login
```python
#Use a python module to handle passwords
from getpass import getpass

username = input('Username: ')
#it will hide the password when inputting
password = getpass('Password: ')
```