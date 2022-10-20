import json
from urllib import response

with open('foto_list.json') as file:
    templates = json.load(file)

# print(templates['response']['items'][0]['sizes'][0]['url'])
short_temp = templates['response']['items'][0]
types = [value for size in short_temp['sizes'] for key, value in size.items() if key == 'type']
print(types)
print(short_temp['sizes'][0]['type'])
