import urllib.request
import json
json_str = urllib.request.urlopen("http://api.giphy.com/v1/gifs/random&tag=husky&api_key=PDek1p3p8vU6HFUV0OR7ttaDtw6LWs9E&limit=1").read()
# print(json_str)
data = json.loads(json_str)
# print(data)
json_output = json.dumps(data, sort_keys=True, indent=4)
json_dict = json.loads(json_output)
print(json_dict['data'][0]['bitly_gif_url'])