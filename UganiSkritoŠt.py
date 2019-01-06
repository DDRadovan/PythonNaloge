# -*- coding: utf-8 -*-
import random

def main():
    secret_num = random.randint(1, 50)

    while True:
        guess = int(raw_input("Guess what number from 1 to 50:"))

        if guess == secret_num:
            print "You guessed it ! Your number is %s ! " % secret_num
            break
        elif guess > secret_num:
            print "Your number is too high!"
        elif guess < secret_num:
            print "Your number is too low."


print main()
