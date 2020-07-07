# exercise is to fetch data by key value pairs with in dictionaries
# create a function to return the above values (key:value)
# create a class and move the code block inside the class

# Import requests
import requests

# # Create class
# class JSON_code:
#
#     def __init__(self):
#         pass
#
#     def freeze(self, d):
#         if isinstance(d, dict):
#             return frozenset((key, self.freeze(value)) for key, value in d.items())
#         elif isinstance(d, list):
#             return tuple(self.freeze(value) for value in d)
#         return d
#
#     def print_data(self):
#         post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#         json_data = post_codes_req.json()
#         for key in json_data:
#             xvalue = json_data.get(key)
#             if type(xvalue) is dict:
#                 for key in json_data["result"]:
#                     if type(xvalue) is dict:
#                         for key in json_data["result"]["codes"]:
#                             print(key, ":", json_data["result"]["codes"].get(key))
#                     else:
#                         print(key, ":", json_data["result"].get(key))
#             else:
#                 print(key, ":", xvalue)
#
# def print_data(self):
#     post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#     json_data = post_codes_req.json()
#     for key in json_data:
#         value1 = json_data.get(key)
#         if type(value1) is dict:
#             # Freeze values of dict1 so it can be used as a iterative key for dict2
#             frozen_dict2 = self.freeze(json_data.get(key))
#             # Using frozen (ex dictionatry1) value to iterate through dict2
#             for key in json_data[frozen_dict2]:
#                 frozen_dict3 = json_data[frozen_dict2].get(key)
#                 if type(frozen_dict3) is dict:
#                     # Freeze values of dict2 so it can be used as a iterative key for dict 3
#                     key2 = self.freeze(json_data[frozen_dict2].get(key))
#                     # Using frozen (ex dictionatry2) value to iterate through dict3
#                     for key in json_data[frozen_dict2][key2]:
#                         # Prints out all values from dict3
#                         print(key, ":", json_data[frozen_dict2][key2].get(key))
#                 # Printing out normal values from dict2
#                 else:
#                     print(key, ":", json_data[value1].get(key))
#         # Printing out normal values from dict1
#         else:
#             print(key, ":", value1)
#
# obj1 = JSON_code()
# obj1.print_data()

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# json_data = post_codes_req.json()

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


class JSONReader:

    # This method uses recursion to loop through all nested dictionary values
    def get_all_values(self, nested_dictionary):  # This is a method
        for key, value in nested_dictionary.items():  # iterate through the key, value pairs in this dictionary
            if type(value) is dict:  # if the value of a key is a dictionary, then you have found a nested dictionary
                self.get_all_values(value)  # recall this method passing in that dictionary to iterate through it
            else:
                print(key, ":", value)  # if the value of the dictionary is not a dict carry on looping through

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se167tq")
type_json = post_codes_req.json()
json_reader = JSONReader()
json_reader.get_all_values(type_json)  # Returns all the values inside a dictionary including any nested dictionaries