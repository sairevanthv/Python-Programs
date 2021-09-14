# Write a program to print your last 2 characters from your name and repeat it from 1 to 10
name = input("Enter your name:")
print(name[-2:])
lastTwo = name[-2:]
for val in range(1,11):
    print (lastTwo*val)
print('------------')