from datetime import datetime
import requests

def getTime():
    time = datetime.now().time()
    time = time.strftime("%I:%M %p")
    print("It's ", time)

def getWeather():
    api = 'http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=04a716d70b54bf5c6c24dbb3dfa5db03&units=metric'
    allData = requests.get(api).json()
    weather = allData['weather'][0]['description']
    temp = allData['main']['temp']
    print(weather, ", ", temp)


mappings = {
    'time' : getTime,
    'weather' : getWeather
}