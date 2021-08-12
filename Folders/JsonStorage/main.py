import requests as re

API_URL = "<api_url>"

# get file
response = re.get(API_URL)
print(response) # <Response [200]>

# convert to json
data = response.json()
# add new data
data["new"] = "newdata"

# update file
update = re.put(API_URL, json=data)
print(update) # <Response [200]>