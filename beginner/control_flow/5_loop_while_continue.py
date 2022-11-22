i = 0
while i < 5:
   print(i)
   i = i + 1
   if i == 3 :
      print('Skip 3')
      continue
      print('This will not be shown')
print('Finished')

print('''---result--- 
0
1
2
Skip 3
4
5
Finished
''')

print('''note:
- while break may end the program right when the conditions match, continue will not stop it but still excluded the matched condition
- Case study: calculate airplane ticket for every person, but ignore if age under 3. Use when needed to loop everything until the end but ignore the condition without stopping the loop
''')
