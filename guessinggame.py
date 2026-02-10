
import random


""" list = [1,2,3,4,5,6,7,8,9,10] """
""" x = int(input("guess a number from 1-10")) """
""" num = random.choice(list) """
""" while x != num: """


guess_history = []
number = random.randint(1,10)
x = int(input("guess a number from 1-10"))


while number != x:
    guess_history.append(x)
    if x > number:
        print(guess_history)
        print("your number is too big!")
    if x < number:
        print(guess_history)
        print("your number is too small!")

    x = int(input("guess again!"))

print(guess_history)
print("YAYAYYAYA CORRECT")


