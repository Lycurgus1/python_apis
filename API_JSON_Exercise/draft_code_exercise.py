import requests

def print_data():
    # Using JSON and API to get JSON dictionary
    post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
    json_data = post_codes_req.json()
    a =
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

# def print_data():
#     post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#     json_data = post_codes_req.json()
#     for key, value in json_data.items():
#         # value1 = json_data.items()
#         if type(value) is dict:
#             for key in json_data[value]:
#                 value2 = json_data["result"].get(key)
#                 if type(value2) is dict:
#                     for key in json_data["result"]["codes"]:
#                         print(key, ":", json_data["result"]["codes"].get(key))
#                 else:
#                     print(key, ":", value2)
#         else:
#             print(key, ":", value)