
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime

API_KEY = "YOUR_API_KEY_HERE"

def get_weather(event=None):
    city = city_entry.get().strip()

    if not city:
        result_label.config(text="Please enter a city name")
        icon_label.config(image="")
        suggestion_label.config(text="")
        return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data.get("cod") != 200:
            result_label.config(text="City not found")
            return

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        cond = data["weather"][0]["description"].lower()

        result_label.config(
            text=f"Temp: {temp}°C\nFeels like: {feels}°C\nCondition: {cond.title()}"
        )

    except:
        result_label.config(text="Error fetching data")

root = tk.Tk()
root.title("Weather App")
root.geometry("300x350")

tk.Label(root, text="Weather App", font=("Arial", 18)).pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)
city_entry.bind("<Return>", get_weather)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

icon_label = tk.Label(root)
icon_label.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

suggestion_label = tk.Label(root, text="")
suggestion_label.pack()

root.mainloop()
