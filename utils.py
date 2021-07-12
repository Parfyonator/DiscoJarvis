from typing import Union

import requests


def get_aqi(city: str) -> Union[str, None]:
    try:
        resp = requests.get(f'http://api.waqi.info/feed/{city.lower()}/?token=demo')

        data = resp.json()

        return data['data']['aqi']
    except Exception:
        return None


def aqi_response(city: str) -> str:
    aqi = get_aqi(city)

    if aqi:
        return f'Air quality index in {city} is {aqi}.'
    else:
        return f'Cannot get AQI for {city}('


def get_time(city: str) -> Union[str, None]:
    # TODO: find some free service. Hardcode for now
    return "12:00"


def time_response(city: str) -> str:
    t = get_time(city)

    if t:
        return f'It is {t} in {city} now.'
    else:
        return f'Cannot get time for {city}('


def get_weather(city: str) -> str:
    # TODO: find some free service. Hardcode for now
    return "sunny"


def weather_responce(city: str) -> str:
    weather = get_weather(city)

    if weather:
        return f'It is {weather} in {city} now.'
    else:
        return f'Cannot get weather for {city}('


if __name__ == '__main__':
    print(aqi_response('kyiv'))
    print(get_time('kyiv'))
    print(get_weather('kyiv'))
