my_user = 'Bogie'               #string
print(my_user + '!')            #same rule as data_type
name = input('Enter name: ')    #a prompt message 'Enter name: ' will appear. Default data_type = string
age = int(input())              #change data_type input to int
age2 = input('Enter age: ')     #string
age3 = int(age2)                #change age 2 to int
x = '2'
y = '4'
z = int(x) + int(y)             #change to int
print(z)                        #will calculate as int
print(x + ' and ' + y)          #string operation

print('''---result--- 
6
2 and 4
''')

print('''note:
-123user = 'Bogie'
a-variable%name = 'Bogie'
#error. don't start var with a number, and only support letters, numbers, underscores
-x = 'Bogie'
x = 2   ---> result x = 2
var data_type depends on what inside. no need to declare this var is int or string
''')
