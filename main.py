# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import some headers that may be used
import time
import unittest


# we are having a function called print_hi, and it will be taking in the variable called name =
def chitChat(name):
    # Use a breakpoint in the code line below to debug your script.
    # this is where the function is being defined, above is the function handle merely, and now here below will be the command line
    # that actually occure
    # when this function is called, it will be printing HI, then the name in which the function should be accepting as a variable
    name = input("What is your name?.\n")
    print('Hello ' + name + " it is nice to meet you.\n")

    # next I will recreate the age scripting from earlier
    year = input("What year were you born?\n")
    currentYear = 2021

    age = currentYear - int(year)
    print('So then you are ' + str(age) + ' years old huh, what a time to be alive.')

    selection = input("\nPick a number to type. 1 or 2.\n")

    if int(selection) == (1):
        print('Congrats, first is the worst.')

    elif int(selection) == (2):
        print('You are still number one in our hearts.')

    else:
        print('I do not understand what you are saying dude.')


# here is where I will define the unit test, later should be called within the mainf ucntion
# initlaize a class called siple test, and then create a function that does the test

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertTrue(False)


# Press the green button in the gutter to run the script.
# if the name of the file is infact main then execute
# since this file is called main, then when i click run everything
# contained within the main funciton will execute

if __name__ == '__main__':
    # this calls the function that was intialized previously, and writes the input to be PyCharm
    chitChat('Trevor')

    # have the program wait before clsing

    # this is where my unit test will occur
    unittest.main()
