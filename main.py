import requests

def get_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")

    if response.status_code == 200:
        data = response.json()
        image_url = data[0]['url']
        return image_url
    else:
        return None

