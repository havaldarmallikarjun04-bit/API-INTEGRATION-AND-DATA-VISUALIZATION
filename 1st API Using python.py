import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "ed0c7a77602af0ffa0ac3c66b7376287"
CITY = 'Mumbai'

URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    dates = []
    temperatures = []
    humidity = []

    for entry in data['list']:
        dates.append(entry['dt_txt'])
        temperatures.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.lineplot(x=dates, y=temperatures, marker='o')
    plt.xticks(rotation=45)
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Date-Time")
    plt.ylabel("Temperature (°C)")

    plt.subplot(1, 2, 2)
    sns.barplot(x=dates, y=humidity, palette="Blues_d")
    plt.xticks(rotation=90)
    plt.title(f"Humidity Forecast for {CITY}")
    plt.xlabel("Date-Time")
    plt.ylabel("Humidity (%)")

    plt.tight_layout()
    plt.show()

else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
