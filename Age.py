#Simple python script to experiment with Jenkins
#This should simply prompt user for their birthyear, and then calculate their age
import time



#define prompt
question = "What year were you born?. \n"

#request response from the user, save result
birthYear = input(question)

#convert it to a number and subtract from currentYear
currentYear = 2021

age = currentYear - int(birthYear)

print("Congratulations you are " + str(age) + " years old.")

#Now I am going to add some changes to the python code, and see what if anything is occuring in Jenkins
question2 = "Pick a number 1 or 2?. \n"

selection = input(question2)

if int(selection) == 1:
    print("Well done, you have selected number 1. ")
elif int(selection) == 2:
    print("Darn, well you're still number 1 in our hearts")
else:
    print("I don't understand")
time.sleep(3)
