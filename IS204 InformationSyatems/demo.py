'''
score = int(input("give me the grade: "))
def get_grade(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

grade = get_grade(score)
print(grade)

'''

'''

count = int(input("Enter the count: "))
theSum = int(input("Enter the sum: "))
average = int(input("enter the average: "))
if count > 0 and theSum // count > 10:
    print(average > 10)
else:
    print(count, average)
    
'''

'''
theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", theSum)

'''

'''
# Summation with a for loop
theSum = 0
for count in range(1, 100001):
    theSum += count
print(theSum)


# Summation with a while loop
theSum = 0
count = 1
while count <= 100000:
    theSum += count
    count += 1
print(theSum)

'''
'''

theSum = 0.0
while True:
    data = input("Enter a number or just press Enter to quit: ")
    if data == "":
        break
    try:
        number = float(data)
        theSum += number
    except ValueError:
        print("Bad input")
print("The sum is", theSum)

'''
'''
while True:
    number = int(input("Enter the numeric grade: "))
    if 0 <= number <= 100:
        break
    else:
        print("Error: grade must be between 0 and 100")
print(number) 
'''

'''
import random
for roll in range(10):
    print(random.randint(1, 6), end = " ")
    
'''

'''

num = 2


while num <= 20:
    print(num)
    num += 2


print(num)


while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        print("You entered 0")
        break



age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")

'''



import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked")

def display_text():
    user_text = entry.get()
    display_label.config(text=user_text)


root = tk.Tk()
root.title("Welcome to Tkinter")

label = tk.Label(root, text="Welcome to Tkinter", font=('Arial', 14))
label.pack(pady=20)

entry = tk.Entry(root, font=('Arial', 12))
entry.pack(pady=10)

display_button = tk.Button(root, text="Display Text", command=display_text, font=('Arial', 12), bg='#4682B4', fg='white')
display_button.pack(pady=10)

display_label = tk.Label(root, text="", font=('Arial', 14), fg='#00FF00', bg='#36454F')
display_label.pack(pady=20)

button = tk.Button(root, text="Click Me!", command=on_button_click, font=('Arial', 12), bg='#4682B4', fg='white')
button.pack(pady=10)

root.mainloop()




