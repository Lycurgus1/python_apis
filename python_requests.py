#API = application processing interface
# Used to connect to other programs
# In python module called requests interacts with APIs

import requests
from abc import ABC, abstractmethod

# check HTTP/HTTPs 200(success) - 400. 404 = page not found
# response_bcc = requests.get("https://www.bbc.co.uk/news")

# # Prints status code of the website
# print(response_bcc.status_code)
#
# # Prints headers of website, as dictionary. Also content can be checked
# print(response_bcc.headers)/(response_bcc.content)
# # Can check type
# print(type(response_bcc.headers))

# response_bcc = requests.get("https://www.bbc.co.uk/news")
#
# # Iteration 1
# if response_bcc.status_code == 200:
#     print("It worked!")
# elif response_bcc.status_code == 404:
#     print("This page was not found :(")
# else:
#     print("Something went wrong!")

# Iteration 2
# Create functon called check_response.# returns the message with status code

# def check_response():
#     website = input("What url would you like to check?\n")
#     web_status = (requests.get(website)).status_code
#     if web_status == 200:
#         print("You got status code {}, it worked!".format(web_status))
#     elif web_status == 404:
#         print("You got status code {}, this page was not found :(".format(web_status))
#     else:
#         print("You got status code {}, something went wrong!".format(web_status))
#
# check_response()

# 3rt Iteration? OOP with 4 pillars.
# Inheritance

class First_check:

    def __init__(self):
        pass

    def check_response(self):
        website = input("What url would you like to check?\n")
        web_status = (requests.get(website)).status_code
        if web_status == 200:
            print("You got status code {}, it worked!".format(web_status))
        elif web_status == 404:
            print("You got status code {}, this page was not found :(".format(web_status))
        else:
            print("You got status code {}, something went wrong!".format(web_status))

    def __hidden_function(self):
            print("Not everyone can access this class")

    # Abstract method defines a method that must be included in the the parent classes
    @abstractmethod
    def more_information(self):
        pass

class Further_information(First_check):

    def _init__(self):
        pass

    def more_information(self):
        print("Websites don't work for a variety of reasons, have you checked the spelling?")
        code = int(input("What status code do you want to know about?\n"))
        if code == 200:
            print("200 means the website is running!")
        elif code == 400:
            print("400 happens when the server thinks you made a bad request")
        elif code == 403:
            print("403 means that the resource you are trying to access is forbidden")
        elif code == 404:
            print("404 is when the website was not found")
        else:
            print("Sorry I don't what {} means".format(code))

    def check_response(self):
        print("This is slightly different to the parent function of the same name")
        website = input("What url would you like to check?\n")
        web_status = (requests.get(website)).status_code
        if web_status == 200:
            print("You got status code {}, it worked!".format(web_status))
        elif web_status == 404:
            print("You got status code {}, this page was not found :(".format(web_status))
        else:
            print("You got status code {}, something went wrong!".format(web_status))

# Creating object of child class
obj1 = Further_information()

# Creating object of parent class
obj2 = First_check()

# This function is private in the parent class so a child class obejct cannot use it. (Encapsulation)
# obj1.__hidden_function()

# The method from the parent class has been inherited by the child class (Inheritance)
# obj1.check_response()

# There is two methods of the same name, in child class it overrides the parent class function (Polymorphism)
# obj1.check_response()
# obj2.check_response()

obj1.more_information()