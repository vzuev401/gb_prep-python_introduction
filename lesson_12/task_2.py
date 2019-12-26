import json
import pickle
from pathlib import Path
from pprint import pprint


def read_from_file_and_deserialize(_path):
    file_bytes = _path.read_bytes()
    try:
        _data = json.loads(file_bytes)
    except UnicodeDecodeError:
        _data = pickle.loads(file_bytes)

    return _data


path = Path('files')
filename_template = 'my_*'


for matching_path in path.glob(filename_template):
    data = read_from_file_and_deserialize(matching_path)

    print(f'File: {matching_path}\nData: ')
    pprint(data)

