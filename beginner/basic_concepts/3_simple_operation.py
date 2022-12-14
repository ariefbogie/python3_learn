print("Hello "+'World!')
print("Hi"*3)             #print Hi 3 times
print("Hi "+"2")          #string
print("Hi "+str(2*2))     #string
print(2+2)                #int. also int using *
print(2+2.0)              #float. Also float using *
print(4/2)                #float. / = float

print('''---Result---
Hello World!
HiHiHi
Hi 2
Hi 4
4
4.0
2.0
''')

print{'''--Note--
- print("Hello "+2) --> SyntaxError. Text data types can't do (+,- or /) with number data types, but can do (*).
- however, print("Hi "+str(2*2)) ---> works, as 4*4 was calculated before converting it to string
- every number calculation involves any float, always results in float
- every number calculation involves (/), always results in float
''')
