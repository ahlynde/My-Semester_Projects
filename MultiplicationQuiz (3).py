#Amelie Lynde
#1/8/25
#Multiplication Quiz
#Init
import random
import time
score = 0 #Global
#Functions
def quiz():
    global score
    print("Welcome to the Multiplication Quiz Game")
    amount = int(input("How many questions would you like on your quiz?"))
    for i in range(amount):
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print("What is " + str(num1) + "*" + str(num2))
        start_time = time.time()
        question = input("Enter your answer")
        print("Your answer: " + str(question))
        ans = num1*num2
        if num1 * num2 == question:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect, the correct answer is " + str(ans))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Good Job! You got " + str(score) + "/" + str(amount) + " correct!")
    print("You completed the quiz in " + str(elapsed_time) + " seconds")

#Main
quiz()
