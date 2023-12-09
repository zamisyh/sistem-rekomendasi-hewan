import json

file = open('data.json')
data = json.load(file)

for i in data:
    print(i)


file.close()