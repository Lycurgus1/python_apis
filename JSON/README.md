# JSON
- Javascript object notation
    - Independent language
    - Syntax for exchanging information
    - Data comes in key value pairs, seperated by commas:
```
{"Cheese": "Brie", "Meat": "Salami"}
```

- Uses dump, dumps to encode. Do similar things slightly differently (JSON to python):
```python
# Creating JSON object- json.dumps changes python dict to json str
# Just to illustrate theory
car_data_json_string = json.dumps(car_data)
# Data type has changing
print(type(car_data_json_string))
```
```python
# Create JSON file with writing permision - W = write. Column aliasing at end
with open("new_json_file.json", "w") as jsonfile:
    # Dump method takes two args. First one is dictionary created. Second is the file object
    json.dump(car_data, jsonfile)
```
- Uses load to decode (python to JSON):
```python
    def conversion(self):
        with open("exchange_rates.json", "r") as jsonfile:
            self.dataset = json.load(jsonfile)
```

- HTTP Data types: What we get back in JSON file from request
    - Header
    - Content
    - Status
    - Text
    - Object 
    - Dictionary(Array in other languages)
    
- Come from URL as part of request
    - Javascript
    - Xml
    - Html
     
- Http response
    - Header (data in key value pairs)
    - Response code (200, 404 etc.)
    - Body (Text, Json, XML)
    