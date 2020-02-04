print("Welcome to the random password generator.")
name= input("What is your name?")
print("Welcome" +name)

import random
import string

def randomPassword():

    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random .choice(string.punctuation)

    for i in range(6):
        password += random.choice(randomSource)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print ("Random Password 1 is ", randomPassword())
print ("Random Password 2 is ", randomPassword())
print ("Random Password 3 is ", randomPassword())
