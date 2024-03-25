import json


def load_update():
    try:
        file_version = open('../data/version.json', 'r')
        data = json.load(file_version)
        version = data['version']
        return version
    except:
        return None
