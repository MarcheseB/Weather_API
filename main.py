import requests

API_KEY = 'f86453adece2520649b44febc22e3aa0'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input("Enter a city name: ")
# In the url, I added '&units=metric' to change the temerature unit to celsius and '&lang=pt_br' to change the
# language to brazilian portuguese, so that I don't needd to worry about doing conversions
url = f'{BASE_URL}?appid={API_KEY}&q={city}&units=metric&lang=pt_br'
response = requests.get(url)

# To check if there's any erros getting the API -> 200 means that is ok
if response.status_code == 200:
    data = response.json()
    # Printing the data it self helps to understand the following setps
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Clima: {weather}\nTemperatura: {temperature}°C")

else:
    print("An error occurred.")