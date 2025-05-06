'''
Taylor Borden
IS204 9/19/2024
'''





# 1 print 1 - 20 incrementing by 2


num = 2
while num <= 20:
    print(num)
    num += 2
print(num)





# 2 keeps asking me to enter numbers but when i enter 0 it stops

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        print("You entered 0")
        break



# 3 age check 


age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")
