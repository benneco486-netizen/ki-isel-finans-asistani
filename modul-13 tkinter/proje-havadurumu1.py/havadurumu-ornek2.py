import tkinter as tk
import requests
import time

def getWeather(event=None):
    city = textfield.get()

    # 1. Şehri koordinata çevir
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=tr"
    geo_data = requests.get(geo_url).json()

    if not geo_data.get("results"):
        label1.config(text="Şehir bulunamadı!")
        label2.config(text="")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    # 2. Hava durumunu al
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,"
        f"weather_code,surface_pressure"
        f"&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset"
        f"&timezone=auto&forecast_days=1"
    )
    data = requests.get(weather_url).json()
    current = data["current"]
    daily = data["daily"]

    wmo_codes = {
        0: "Açık", 1: "Çoğunlukla Açık", 2: "Parçalı Bulutlu", 3: "Kapalı",
        45: "Sisli", 48: "Sisli", 51: "Çisenti", 61: "Yağmurlu",
        71: "Karlı", 80: "Sağanak", 95: "Fırtınalı"
    }
    condition = wmo_codes.get(current["weather_code"], "Bilinmiyor")
    temp     = int(current["temperature_2m"])
    max_temp = int(daily["temperature_2m_max"][0])
    min_temp = int(daily["temperature_2m_min"][0])
    pressure = int(current["surface_pressure"])
    humidity = current["relative_humidity_2m"]
    wind     = current["wind_speed_10m"]
    sunrise  = daily["sunrise"][0].split("T")[1]
    sunset   = daily["sunset"][0].split("T")[1]

    label1.config(text=f"{condition}\n{temp}°C")
    label2.config(text=(
        f"\nMaksimum Sıcaklık: {max_temp}°C"
        f"\nMinimum Sıcaklık: {min_temp}°C"
        f"\nBasınç: {pressure} hPa"
        f"\nNem: {humidity}%"
        f"\nRüzgar Hızı: {wind} km/h"
        f"\nGün doğumu: {sunrise}"
        f"\nGün batımı: {sunset}"
    ))

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Hava Durumu")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()