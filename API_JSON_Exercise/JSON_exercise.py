# exercise is to fetch data by key value pairs with in dictionaries
# create a function to return the above values (key:value)
# create a class and move the code block inside the class

# Import requests
import requests

# Create class
class JSON_code:

    # Intialising class, then passing
    def __init__(self):
        pass

    # Creating method
    def print_data(self):
        # Using JSON and API to get JSON dictionary
        post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
        json_data = post_codes_req.json()
        # For loop going through 1st dictionary
        for key in json_data:
            value1 = json_data.get(key)
            # If loop for 1st dictionary, either prints values/keys or sends to other for loop if they are dictionary
            if type(value1) is dict:
                # For loop going through 2nd dictionary
                for key in json_data["result"]:
                    value2 = json_data["result"].get(key)
                    # If loop for 2nd dictionary, either prints values/keys or sends to other for loop if they are dictionary
                    if type(value2) is dict:
                        # For loop going through 3rd dictionary
                        for key in json_data["result"]["codes"]:
                            # Printing keys and values in 3rd dictionary
                            print(key, ":", json_data["result"]["codes"].get(key))
                    else:
                        # Print keys and values in 2nd dictionary
                        print(key, ":", value2)
            else:
                # Print keys and values in 1st dictionary
                print(key, ":", value1)
# Creating class object
obj1 = JSON_code()
# Calling method
obj1.print_data()

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# json_data = post_codes_req.json()

# class JSONReader:
#
#     # This method uses self refferal to loop through all dictionary values, from all nested dictionaries
#     def get_all_values(self, nested_dictionary):
#         # iterate through the key, value pairs in this dictionary
#         for key, value in nested_dictionary.items():
#             # if the value of a key is a dictionary, then you have found a nested dictionary
#             if type(value) is dict:
#                 # self recall the method in the nested dictionary to iterate through it
#                 self.get_all_values(value)
#             # Otherwise the key, value key will print normally
#             else:
#                 print(key, ":", value)  # if the value of the dictionary is not a dict carry on looping through
#
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se167tq")
# type_json = post_codes_req.json()
# json_reader = JSONReader()
# json_reader.get_all_values(type_json)  # Returns all the values inside a dictionary including any nested dictionaries

# # Code sample to test what code is needed in individal parts of the method
# for key in json_data:
#     xvalue = json_data.get(key)
#     if type(xvalue) is dict:
#         for key in json_data["result"]:
#             print(key, ":", json_data[key].get(key))
#     else:
#         print(key, ":", xvalue)

# for key in json_data["result"]:
#     print(key, ":", json_data["result"].get(key))
# # print(type(json_data["result"]))
# print(json_data["result"])
# # print(json_data)