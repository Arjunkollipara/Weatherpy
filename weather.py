from ttkbootstrap import ttk as ttkbootstrap
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

//we are using the openweather api to get the data here
def get_weather(city):
    API_key = "USE_YOUR_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("ERROR!", "City NOT Found")
        return None

    weather_data = res.json()

    return {
        'icon_url': f"https://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png",
        'temperature': weather_data['main']['temp'] - 273.15,
        'description': weather_data['weather'][0]['description'],
        'city': weather_data['name'],
        'country': weather_data['sys']['country'],
        'weather_id': weather_data['weather'][0]['id'],
    }


def update_background_color(weather_id):
    color_mapping = {
        800: '#87CEEB',
        801: '#87CEEB',
        802: '#778899',
        803: '#778899',
        804: '#778899',
        500: '#4682B4',
        501: '#4682B4',
        502: '#4682B4',
        503: '#4682B4',
        504: '#4682B4',
        511: '#FFFAFA',
        600: '#FFFAFA',
        601: '#FFFAFA',
        602: '#FFFAFA',
        611: '#FFFAFA',
        612: '#FFFAFA',
        613: '#FFFAFA',
        615: '#FFFAFA',
        616: '#FFFAFA',
        620: '#FFFAFA',
        621: '#FFFAFA',
        622: '#FFFAFA',
    }
    default_color = '#FFFFFF'

    color = color_mapping.get(weather_id, default_color)

    root.configure(bg=color)


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    update_background_color(result['weather_id'])

    location_label.configure(text=f"{result['city']}, {result['country']}")

    image = Image.open(requests.get(result['icon_url'], stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon
    temperature_label.configure(text=f"Temperature: {result['temperature']:.2f}°C")
    description_label.configure(text=f"Description: {result['description']}")


root = tk.Tk()
root.title("My Weather App")
root.geometry("600x500")

city_entry = ttkbootstrap.Entry(root, font="Helvetica 18")
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=search)
search_button.pack(pady=10)

location_label = tk.Label(root, font="Helvetica 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica 25")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica 25")
description_label.pack()

root.mainloop()
