x = "Hello"
y = 5
print(x)
name = input("Enter your name: ")
print("Hello ", name)
birthyear = int(input("Enter your birth year: "))
bday = input("Have you had your birthday this year? ")
if bday == "yes":
    age = 2025 - birthyear
    print("Your age is ", age)
elif bday == "no":
    age = 2024 - birthyear
    print("Your age is ", age)
else:
    print("Invalid")