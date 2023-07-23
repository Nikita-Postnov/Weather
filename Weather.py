import tkinter as tk
from tkinter import messagebox
import requests


def get_weather():
    city = city_entry.get()
    api_key = '8798bcb86f710394c41b72ebdb20ff1e'  # Замените YOUR_API_KEY на ваш API ключ OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            weather_label.config(text=f'Temperature: {temperature}°C\nDescription: {description}')
        else:
            messagebox.showerror('Error', 'City not found or invalid API key.')
    except requests.ConnectionError:
        messagebox.showerror('Error', 'Connection Error.')


# Создание графического интерфейса
root = tk.Tk()
root.title('Weather App')
root.geometry('300x200')

city_label = tk.Label(root, text='Enter city name:')
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text='Get Weather', command=get_weather)
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text='')
weather_label.pack()

root.mainloop()
