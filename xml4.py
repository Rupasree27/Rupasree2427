import xmltodict
import json

 

user_data = input("Enter the xml data:\n")

 

json_data = json.dumps(xmltodict.parse(user_data), indent = 4)

 

 

print(json_data)
