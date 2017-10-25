import json

with open("helloworld.json") as file:
    a = json.load(file)
    for a,b in a.items():
        print(a,b)

