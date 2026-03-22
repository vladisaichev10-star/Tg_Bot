import requests

BASE_URL = "https://api.poiskkino.dev/"
KINOPOSK_API = "C2STSBP-QRQ4P9J-HW3ZD3T-AHHQXH5"


HEADERS = {"X-API-KEY":KINOPOSK_API}


def awards():
    response = requests.get(url="https://api.poiskkino.dev/v1.4/movie/awards",
                            headers=HEADERS)

    print(response.json())
    print(response.status_code)


def random_film():
    response = requests.get(url="https://api.poiskkino.dev/v1.4/movie/random",
                            headers=HEADERS)

    full_info = response.json()
    film_info = _info(data=full_info)

    return film_info

def _info(data: dict):
    print(data)
    name = data.get("name")
    _type = data.get("type")
    description = data.get("description")
    year = data.get("year")

    poster_data = data.get('poster')

    # Если постер словарь, забрать строку из словаря
    if isinstance(poster_data, str):
        poster = poster_data
    elif isinstance(poster_data, dict) and 'url' in poster_data:
        poster = poster_data.get("url")
    else:
        poster = None

    message = (f"ИМЯ: {name}\n"
               f"Тип: {_type}\n"
               f"Описание: {description}\n"
               f"Год: {year}\n"
               f"{poster}")

    return message

if __name__ == '__main__':

    print(random_film())