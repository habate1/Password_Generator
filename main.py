import random
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()<>?;:,._-|"
password = ""

length = int(input("Enter a length for password: "))
count = int(input("Enter how many passwords you would like: "))

for x in range(count):
    password = ""
    for x in range(length):
        password += random.choice(chars)
    print("Here is your generated password: ", password)