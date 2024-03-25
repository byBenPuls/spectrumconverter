import json


def load_update():
    try:
        """file_version = open('../data/version.json', 'r')
        data = json.load(file_version)
        version = data['version']"""
        version = '1.05'
        return version
    except:
        return None
