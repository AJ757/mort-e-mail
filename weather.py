import requests
from datetime import datetime

weather_codes= {
    0: "Clear sky", 1: "Mainly clear",  2: "Partly cloudy",  3: "Overcast",  45: "Fog", 
    48: "Depositing rime fog",  51: "Light drizzle",  53: "Moderate drizzle",  55: "Dense drizzle",  
    56: "Light freezing drizzle", 57: "Dense freezing drizzle", 61: "Slight rain", 63: "Moderate rain",
    65: "Heavy rain", 66: "Light freezing rain", 67: "Heavy freezing rain", 71: "Slight snow fall",
    73: "Moderate snow fall", 75: "Heavy snow fall", 77: "Snow grains", 80: "Slight rain showers",
    81: "Moderate rain showers", 82: "Violent rain showers", 85: "Slight snow showers", 
    86: "Heavy snow showers", 95: "Thunderstorm (slight or moderate)", 96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

def forecast_7days(lat,lon):
    api_url=f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=auto'

    response = requests.get(api_url)
    data = response.json()
    dates = data['daily']['time']
    codes = data['daily']['weather_code']
    desc = [ weather_codes.get(code,"Unknown") for code in codes]
    max_min = list(zip(data['daily']['temperature_2m_max'],data['daily']['temperature_2m_min']))
    # print("Date".center(10),"Day".center(10),"Max".center(6),"Min".center(6),"Description")
    # for k in range(7):
    #     date = dates[k]
    #     day = datetime.strptime(date,"%Y-%m-%d").strftime("%A")
    #     wc = weather_codes.get(codes[k],"Unknown")
    #     print(f'{date:<10} {day:<10} {max_min[k][0]:<6} {max_min[k][1]:<6} {wc}')
    return {'today max': max_min[0][0],
            'today min':max_min[0][1],
            'today description':desc[0],
            'week dates':dates,
            'week description':desc}
