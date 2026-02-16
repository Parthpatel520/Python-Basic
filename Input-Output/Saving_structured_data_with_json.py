import json

Data = {
    "name":"parth",
    "age": 22,
    "city": "surat" 
}

with open("data.json", "w") as file:
    json.dump(Data, file)
    
Data["skill"] = ["python", "JavaScript"]
    
with open("data.json", "w") as file:
    json.dump(Data, file)
    
with open("data.json", "r") as f:
    loaded_data = json.load(f)   # load = read JSON and convert to Python object

print(loaded_data)
