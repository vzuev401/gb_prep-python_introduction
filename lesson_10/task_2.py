import random


def get_random_element(_list):
    if not _list:
        return None
    return random.choice(_list)

