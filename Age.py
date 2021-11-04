#Simple python script to experiment with Jenkins
#This should simply prompt user for their birthyear, and then calculate their age

#define prompt
question = "What year were you born?. \n"

#request response from the user, save result
birthYear = input(question)

#convert it to a number and subtract from currentYear
currentYear = 2021

age = currentYear - int(birthYear)

print("Congratulations you are " + str(age) + " years old.")

