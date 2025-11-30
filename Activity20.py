 import random

print("number guessing game")
print("++++++++++++++++++++++++++++++")

random_value = random.randint(1,100)
tries = 0 
tuloy = True 

name = input("input your name -->")

while tuloy == True:
        num = eval(input("guess a number from 1 to 100 --> "))

        if num == random_value:
                tries +=1
                print("winner !!!")
                print(f"hi {name}, your guess is correct, number of tries")
for x in range(1,11,1):
        for a in range(1,x,1):
                print(" ", end=" ")
        for b in range(10,x,-1):
                print("*", end=" ")
        for c in range(10,x,-1):
                print("*", end=" ")
        print("*")
