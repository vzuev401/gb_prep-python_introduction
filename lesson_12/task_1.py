import json
import pickle
from pathlib import Path


def serialize_and_write_to_file(_path, _package, _content):
    if type(dump := _package.dumps(_content)) == bytes:
        _path.write_bytes(dump)
    elif type(dump) == str:
        _path.write_text(dump)
    else:
        print('_content must be str or bytes')
        return False

    print(
        f'Data is successfully serialized with {_package}\n'
        f'Path: {_path.absolute()}\n'
    )
    return _path


my_favourite_radio = {
    'name': 'Open Lab',
    'site': 'https://openlab.fm/',
    'broadcasting': {
        'online': 'https://openlab.fm/',
        'fm': '106.4FM in Ibiza and Formentera',
    },
    'genres': [
        'electronic',
        'alternative',
        'ambient',
        'experimental',
        'chillout',
        'modern classical',
        'soul',
        'jazz'
    ]
}

filename = 'my_favourite_radio'
path = Path('files')

for package in (pickle, json):
    serialize_and_write_to_file(
        path.joinpath(f'{filename}.{package.__name__}'),
        package,
        my_favourite_radio,
    )
