i = 0
while True:               #default: true
   print(i)
   i = i + 1
   if i == 3 :
      print('Breaking')
      break
print('Finished')

print('''---result--- 
0
1
2
Breaking
Finished
''')

print('''note:
- remember to add a colon : after ehile condition
- while break may end the program right when the conditions match, continue will not stop it but still excluded the matched condition
- Case study: selecting a suitable GYM plan. Use when needed to loop as far as possible but stop the loop when already fit the rule
''')
