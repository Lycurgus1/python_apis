# JSON
- Javascript object notation
- Independent language

```
{"Cheese": "Brie", "Meat": "Salami"}
```

- Data separated by commas
- Code block example

```
import json

# Encoding data and writing in json file
car_data = {"Name" : "Renault", "Country" : "France"} # Dictionary
# Testing code
for i in enumerate(car_data.items()):
    print(i)

print(car_data.get("Name"))
# Finding out data type
print(type(car_data))

# Creating JSON object- json.dumps changes python dict to json str
# Just to illustrate theory
car_data_json_string = json.dumps(car_data)
# Data type has changing
print(type(car_data_json_string))

# Create JSON file with writing permision - W = write. Column aliasing at end
with open("new_json_file.json", "w") as jsonfile:
    # Dump method takes two args. First one is dictionary created. Second is the file object
    json.dump(car_data, jsonfile)

# Encoding and creating into JSON file. Car_data converted into string by

# Decoding
with open("new_json_file.json") as jsonfile:
    # Reading from file I just created
    # Storing data from file to car variable. This is parsing
    car = json.load(jsonfile)
    # Checking/testing data
    print(type(car))
    print(car["Name"])
    # Different dictionary method for practice
    print(car.get("Country"))
```