#api in content acces
import requests

lat = 1.29
lon = 36.82

api_key="5997bfdb752b4a69ea8303f98afcc2b9"
url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response= requests.get(url)
# print(response.status_code)

data = (response.json())

coordinates= data['coord']

print("Longitude:", coordinates['lon'])
print("Latitude:", coordinates['lat'])
