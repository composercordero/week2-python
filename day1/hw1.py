# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

list_num = []

num = 0

while num ** 3 < 1001:
    list_num.append(num ** 3)
    num += 1
    
print(list_num)

# Get first prime numbers up to 100

prime = []

for i in range(2,100):
    for j in range(2,100):
        if i%j == 0:
            break
    if i == j:
        prime.append(i)

print(prime)


# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

user_input = input("Enter your age: ")

if int(user_input) > 0:
    if int(user_input) > 65:
        print('seniors')
    elif int(user_input) >= 18:
        print('adults')
    else:
        print('kids')
else:
    print('Enter a number > 0')