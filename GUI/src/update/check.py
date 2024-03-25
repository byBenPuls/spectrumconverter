import requests


def check_update():
    try:
        response = requests.get(
            'https://raw.githubusercontent.com/byBenPuls/spectrumconverter/main/GUI/data/version.json')
        if response.status_code == 200:
            data = response.json()['version']
            return data
        else:
            return None
    except Exception as e:
        print("Update is not available\n{}".format(str(e)))
