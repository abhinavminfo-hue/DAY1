num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
numbers= [num1, num2, num3, num4]

large = numbers[0]
small = numbers[0]
for number in numbers:
    if number > large:
        large= number
    elif number < small:
        small = number

print("Large: ", large)
print("Small: ", small)


# Q.2
year = int(input("Enter current year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not leap")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not also leap")


# Q.3
side1 = int(input("Enter side 1:"))
side2 = int(input("Enter side 2:"))
side3 = int(input("Enter side 3:"))
if not side1 + side2 >  side3  and side1 + side3 > side2 and side2 + side3 > side1:
    print("Invalid triangle ")
if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles")
else:
    print("Scalene")

# Q.4
Username =  "admin"
Password =  "python123"
name = input("Enter username: ")
password = input("Enter password: ")
if name != Username:
    print("User not found")
elif password != Password:
    print("Wrong Password")
else:
    print("Login Successful")




# Q.6
number = int(input("Enter a number: "))
print("Input:", number)

if number > 0:
    print("Positive:", number)
elif number < 0:
    print("Negative:", number)

else:
    print("Zero:", number)

# Q.7
number  = int(input("Enter a number: "))
print("Input: ", number)

if number > 0 and number % 2 == 0:
    print("Output: Positive and Even")
elif number > 0 and number % 2 != 0:
    print("Output: Positive and Odd")
elif number < 0 and number % 2 == 0:
    print("Output: Negative and Even")
elif number < 0 and number % 2 != 0:
    print("Output: Negative and Odd")
else:
    print("Output: Zero")


# Q.8
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("Enter aritmetic operator: ")
print("Enter first numeber: ", num1)
print("Enter second number: ", num2)
print("Enter operator: ", operator)
if operator == "+":
    print("Output: ", num1 + num2)
elif operator == "-":
    print("Output: ", num1 - num2)
elif operator == "*":
    print("Output: ", num1 * num2)
elif operator == "/":
    print("Output: ", num1 / num2)
elif operator == "%":
    print("Output: ", num1 % num2)
else:
    print("Invalid operator")


# Q.9
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
numbers = [num1 ,num2 ,num3]

large = numbers[0]
for number in numbers:
    if number > large:
        large = number
print("Output: \n", large)



# Q.10
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
if num % 2 == 0:
    print("Even")
elif num % 2 != 0:
    print("Odd")

if num % 5 == 0:
    print("Divisible by 5")
elif num > 100:
    print("Greater than 100")


# Q.11
num = int(input("Enter a number:"))
print("Input: ", num)
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
if num % 2 == 0:
    print("Even")
elif num % 2 != 0:
    print("Odd")
if num % 3 == 0:
    print("Divisible by 3")
if num % 5 == 0:
    print("Divisible by 5")
if num > 100:
    print("Greater than 100")


# Q.12
print("  ==== Student result analyzer ====  ")
name = input("Enter your name: ")
print("Name of the student", name)
total_marks = 700
maths = int(input("Enter your Maths marks: "))
physics = int(input("Enter your Physics marks: "))
english = int(input("Enter your English marks: "))
computer = int(input("Enter your Computer marks: "))
chemistry = int(input("Enter your chemistry marks: "))
print("Maths: ", maths)
print("Physics: ", physics)
print("English: ", english)
print("computer: ", computer)
print("Chemistry: ", chemistry)
marks = [maths, physics, english, computer, chemistry]
total = 0
for mark in marks:
    total += mark
percentage = float(total / total_marks * 100)
print("Total", total)
print("Percentage: ", percentage)
if maths < 33 or physics < 33 or chemistry < 33 or english < 33 or computer < 33:
    print("Result: Fail")
else:
    print("Result: Pass")
if percentage > 90:
    print("A Grade")
elif percentage > 75 and percentage < 89:
    print("B Grade")
elif percentage > 60 and percentage < 74:
    print("C Grade")
elif percentage > 50 and percentage < 59:
    print("D Grade")
else:
    print("E Grade")


# Q.13
print("==== Number Digit Analyzer ====")
num = int(input("Enter a three digit number : "))
if 3 >= len(num):
    print("Invalid number")
else:
    hun = print("Hundred digit: ", num // 100)
    ten = print("Tens digit: ", (num // 10) % 10)
    unit = print("Units digit: ", num % 10)
    number = [hun, ten, unit]
    total = print("Sum:", sum(number))
    reverse = print("Reverse: ", unit, ten, hun)
    

# Q.14
balance = 5000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Balance: ", balance)
if choice == 2:
    deposit_amount = int(input("Enter deposit amount: "))
    if balance < deposit_amount:
        print("Insufficient amount")
    else:
        balance += deposit_amount
print("Deposit amount: ", deposit_amount)
if choice == 3:
    withdraw_amount = int(input("Enter withdraw amount: "))
    if withdraw_amount >= 0 and withdraw_amount < balance:
        print("Withdraw amount: ", withdraw_amount)
    else:
        print("Something went wrong")


# Q.15
password_T = "python123"
password_F = "12345678"
password = input("Enter password: ")
if len(password) < 8:
    print("Too Short")
else:
    print("Valid Length")
    if password == password_T:
        print("Oytput: Strong Password")
    elif password == password_F:
        print("Output: Weak Password")
    else:
        print("Normal Password")


# Q.16
num = int(input("Enter a number: "))

if num < 0:
    print("Input: ", num)
    print("Output: Negative")
elif num >= 0 and num <= 10:
    print("Input: ", num)
    print("Output: Between 0 and 10")
elif num >= 11 and num <= 50:
    print("Input: ", num)
    print("Output: Between 11 and 50")
elif num > 50:
    print("Input: ", num)
    print("Output: Greater than 50")


# Q.17
attendence = int(input("Enter your attendence percentage: "))
if attendence >= 75:
    print("Input: ", attendence)
    print("Eligible for Exam")
elif attendence >= 60 and attendence <= 74:
    print("Input: ", attendence)
    print("Warning")
elif attendence < 60:
    print("Input: ", attendence)
    print("Not Eliginle for Exam")
elif attendence >= 0 and attendence < 100:
    print("Input: ", attendence)
    print("Invalid Attendence")


# Q.18
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif age >= 0 and age <= 5:
    print("Age: ", age)
    print("Free Ticket")
elif age >= 6 and age <= 17:
    print("Age: ", age)
    print("Child Ticket")
elif age >= 18 and age <= 59:
    print("Age: ", age)
    print("Adult Ticket")
elif age >= 60:
    print("Age: ", age)
    print("Senior Citizen Ticket")




