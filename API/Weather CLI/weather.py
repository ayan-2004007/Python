# Built a Weather forcast CLI by using public API


import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
URL=os.getenv("API_URL")
API_KEY=os.getenv("API_KEY")

def displayReport(location,country,tempeature,feelsLike,max,min,humidity,visibility,windSpeed,direction,gust):
    print("="*100)
    print(" "*30,"CURRENT WEATHER REPORT")
    print("="*100)
    print(f"{'Location : ':<50} {location} , {country}")
    print("-"*100)
    print(f"{'Temperature : ':<50} {tempeature}°C ( Feels like : {feelsLike}°C )")
    print(f"{'Maximum Temperature : ':<50} {max}°C")
    print(f"{'Minimun Temperature : ':<50} {min}°C")
    print(f"{'Humidity : ':<50} {humidity}%")
    print(f"{'Visibility : ':<50} {visibility} km")
    print("-"*100)
    print(f"{'Wind Speed : ':<50} {windSpeed} m/s")
    print(f"{'Direction : ':<50} {direction} degree")
    print(f"{'Gust : ':<50} {gust} m/s")
    print("="*100)
    print(" "*30,"Stay safe & have a good day !")
    print("="*100)

def main():
    city=str(input("Enter the city name : ")).lower().strip()
    FullUrl=f"{URL}{city}&appid={API_KEY}&units=metric"
    # print(FullUrl)
    try:
        response=requests.get(FullUrl)
        data=response.json()
        if data["cod"]!=200:
            print("Internal Server Error occured !")
            return
        location=data["name"]
        country=data["sys"]["country"]
        temperature=data["main"]["temp"]
        feelsLike=data["main"]["feels_like"]
        max=data["main"]["temp_max"]
        min=data["main"]["temp_min"]
        humidity=data["main"]["humidity"]
        visibility=int(data["visibility"])/1000
        windSpeed=data["wind"]["speed"]
        direction=data["wind"]["deg"]
        gust=data["wind"]["gust"]

        displayReport(location,country,temperature,feelsLike,max,min,humidity,visibility,windSpeed,direction,gust)
    except Exception as e:
        print(f"Something went wrong : {e}")

if __name__=="__main__":
    main()