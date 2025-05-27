import requests
from conf.settings import URL_WEATHER_API, API_KEY, EMOJI_CODE


def get_weather(lon, lat):
    params = {'lat': lat,
              'lon': lon,
              'lang': 'ru',
              'units': 'metric',
              'appid': API_KEY}
    response = requests.get(url=URL_WEATHER_API, params=params).json()
    city_name = response['name']
    description = response['weather'][0]['description']
    code = response['weather'][0]['id']
    temp = response['main']['temp']
    temp_feels_like = response['main']['feels_like']
    humidity = response['main']['humidity']
    emoji = EMOJI_CODE[code]
    message = f'🏙 Погода в: {city_name}\n'
    message += f'{emoji} {description.capitalize()}.\n'
    message += f'🌡 Температура {temp}°C.\n'
    message += f'🌡 Ощущается {temp_feels_like}°C.\n'
    message += f'💧 Влажность {humidity}%.\n'
    return message
