import requests as req
import pandas as pd
import matplotlib.pyplot as plt
import os 
def weather_finder(long ,lat):
    urll = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"
    response = req.get(urll)
    data = response.json()
    return data ["timezone"], data["current_weather"]["temperature"], data["current_weather"]["windspeed"]

print(weather_finder(77.1025, 28.7041))  # Example coordinates for New Delhi, India

pd_e = pd.DataFrame({
    "longitude": [77.1025, 2.3522, -0.1276],
    "latitude": [28.7041, 48.8566, 51.5074]
})
print(pd_e)

plt.figure(figsize=(10, 6))
plt.plot(pd_e["longitude"], pd_e["latitude"], marker='o', linestyle='-', color='b')
plt.title("Geographical Coordinates")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(["Coordinates"])
plt.grid()

os.makedirs("plots", exist_ok=True)
pd_e.to_csv("plots/coordinates.csv", index=False)
print("Coordinates saved to plots/coordinates.csv") 