# Revision - Input name & age, print sentence
name=input("Enter your Name: ")
age=int(input("Enter your age: "))
print(f"You are {name} and Your {age} ")

# Revision - Input 2 numbers, show sum
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(f"Addition of {num1}+{num2}is: ",(num1+num2))

# Revision - Input name, show length
name=input("Enter your name: ")
print(len(name))

# Revision - Check odd/even
num1=int(input("Enter your number: "))
if num1%2==0:
    print(f"The number {num1} is even")
else:
    print(f"The number {num1} is odd ")

# Revision - Age category: Child, Teen, Adult
age=int(input("Enter your age: "))
if age<18 :
    print("Child")
elif age==18:
    print("Teen")
else:
    print("Adult")

# Revision - Print 1 to 10 using for & while
for i in range(1,11):
    print(i)
i=0
while i<=9:
 i+=1
 print(i)

# revision - Sum 1 to 50
total=0
for i in  range(1,51):
    total=i+total
    print(total)

i=0
total=0
while i<=49:

    total=i+total
    print(total)
    i+=1

# Revision Table of user input
num=int(input("Enter your Number: "))

for i in range(1,11):
    mul=num*i
    print(f"{num}x{i}={mul}")

