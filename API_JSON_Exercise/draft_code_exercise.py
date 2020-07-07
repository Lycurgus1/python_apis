def print_data(self):
    post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
    json_data = post_codes_req.json()
    for key, value in json_data.items():
        # value1 = json_data.items()
        if type(value) is dict:
            for key in json_data[value]:
                value2 = json_data["result"].get(key)
                if type(value2) is dict:
                    for key in json_data["result"]["codes"]:
                        print(key, ":", json_data["result"]["codes"].get(key))
                else:
                    print(key, ":", value2)
        else:
            print(key, ":", value)