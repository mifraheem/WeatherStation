from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
def index(request):

    return render(request, 'weather/index.html')

def checkWeather(request):
    cityName = request.GET.get('city', 'default')
    API = "9c3e11132a734519a31165514232803"
    url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={cityName}"
    
    req = requests.get(url)
    if "error" in req.text:
        params = {"City":cityName}
        return render(request, "weather/error.html", params)
    else:
        weatherDic = json.loads(req.text)

        cName = weatherDic["location"]["name"]
        region = weatherDic["location"]["region"]
        country = weatherDic["location"]["country"]
        tempC = weatherDic["current"]["temp_c"]
        tempF = weatherDic["current"]["temp_f"]
        params = {"City":cName, "Region":region, "Country":country, "cTemp":tempC, "fTemp": tempF}
        return render(request, "weather/weather result.html", params)

def userMessage(request):
    userName = request.GET.get("Name", "default")
    userEmail = request.GET.get("Email", "default")
    userSubject = request.GET.get("Subject", "default")
    userMessage = request.GET.get("Message", "default")
    print(f"{userName} \n {userEmail} \n {userSubject} \n {userMessage} \n")
    return render(request, "weather/message.html")