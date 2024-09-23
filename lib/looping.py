#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
        
    print("Happy New Year!")





def square_integers(int_list):
    new_squares = [x*x for x in int_list]  
    return new_squares



def fizzbuzz():
   
    for x in range(1, 101):
        if x % 15 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

   


