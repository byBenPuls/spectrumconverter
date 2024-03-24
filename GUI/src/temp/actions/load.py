import json

def SaveNewPath(file_path: str):
    with open('../files.json', 'a+', encoding='utf8') as write_file:
        data = json.load(write_file)
        print(data)
        data['FilePath'].append(file_path)
        json.dump(data, write_file)