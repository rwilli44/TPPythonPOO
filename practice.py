import json
import requests 
# data = {
#     "president": {
#         "species": "Betelgeusian",
#         "name": "Zaphod Beeblebrox"
        
#     }
# }

# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)
    
# json_string = json.dumps(data)

# print(json.dumps(data))
# print(json.dumps(data, indent=4))

# print(json.dumps(data, indent=4,separators=(",", ":"),sort_keys=True))

# json_string2 = """
# {
#     "researcher": {
#         "name": "Ford Prefect",
#         "species": "Betelgeusian",
#         "relatives": [
#             {
#                 "name": "Zaphod Beeblebrox",
#                 "species": "Betelgeusian"
#             }
#         ]
#     }
# }
# """
# data2 = json.loads(json_string)
# print(type(data2))
# print(type(json.dumps(data2)))

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# print(type(todos[0]))
