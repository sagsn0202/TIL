from darksky import forecast

multicampus = forecast('4b4008c2618ebdcca85cfdc85a3e8ca3', 37.5014852, 127.0374493)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])

# import requests

# url = "https://api.darksky.net/forecast/4b4008c2618ebdcca85cfdc85a3e8ca3/37.5014852,127.0374493"

# res = requests.get(url)
# data = res.json()