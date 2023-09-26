import sys
import time

def gap():
    time.sleep(1.8)

def program():
    print("Hello my name is Susan from space")
    gap()
    print("What is your name?")

    name = input("enter your name: ")

    print(f"Hello, {name}! I am from the year 2210 and i am 20 years old!")
    gap()
    print("How old are you?")

    age = input("insert your age: ")
    age = int(age)

    future_age = (age + (2210 - 2020))

    print(f"Wow! By 2210 you will be {future_age}! That is really old.")
    gap()
    print("What kind of music are you into?")

    music = input("insert music: ")

    print(f"I have not heard of {music}")
    gap()
    print(f"I will take over the world. Starting with your body, {name}!")
    gap()
    print("YOU DIED")
    gap()
    print("Would you like to try again? (y/n)")
    
    choice = input()
    if choice == y:
        program()
    elif choice == n:
        sys.exit(0)

program()