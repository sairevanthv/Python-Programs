   # write a program to find vowels and constant in your name 
# name = input("Enter you name:")
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# for sum in name:
#     if sum in vowels:
#         print(sum,'- It is a vowel')
#     else:
#         print('- It is a Consonent',sum)

name = input("Enter you name:")
vowels = ['a','e','i','o','u','A','E','I','O','U']
for sum in name:
    if sum in vowels:
        print(sum,'- It is a vowel')
        break



'''
                    Control Statements
Break
Continue
pass

break: Returns control out of the loop directly
continue: Returns control to the begginning of the loop
pass: Used as a placeholder for future implementation of loops,functions etc.
'''
