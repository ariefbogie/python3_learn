print('Bogie\'s \t mother:')   #\' = print ' (backslash). \t = tab
print('One\nTwo\nThree')   #multiple newline
print(r'One\nTwo\nThree')   #r before ' = ignore all processing, displayed as is
print('''this
  is a
multiline''')   #multiline, displayed as is including space, enter

print('''---Result---
Bogie's mother:
One
Two
Three
One\nTwo\nThree
this
  is a
multiline
''')

print('''--Note--
- line 1 backslash followed by single quote is used to print (') without breaking the string
- line 1 (\t) is used to add tab 
- line 2 (\n) is used to add multiple newline, as (\n) add enter
- line 3 by putting r before quote(s) will print the string as is ignoring all processing code
- line 4 is a miltiline
''')
