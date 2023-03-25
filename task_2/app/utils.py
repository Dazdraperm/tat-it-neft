from typing import List
from path import Path


def get_urls(abspath: Path) -> List:
    """Получение ссылок на сайты из файла"""

    filename = 'urls.txt'
    path = abspath / filename
    urls = []

    with open(path, 'r') as file:
        for string in file:
            url = string.split('\n')[0]
            urls.append(url)

    return urls
