import requests as req

def weather_finder(long ,lat):
    urll = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"
    response = req.get(urll)
    data = response.json()
    return data

print(weather_finder(77.1025, 28.7041))  # Example coordinates for New Delhi, India