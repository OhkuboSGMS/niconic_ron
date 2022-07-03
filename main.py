import argparse
from typing import List
from yt_dlp import YoutubeDL


def read_list(file_path: str) -> List[str]:
    try:
        with open(file_path, encoding='UTF-8') as fp:
            return fp.readlines()
    except Exception as e:
        print(e)
        return []


def main(file_path: str):
    url_list = read_list(file_path)
    YoutubeDL()
    option = {'paths': {'home': 'nc'}}
    with YoutubeDL(option) as ydl:
        ydl.download(url_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_list', default='list.txt', type=str)
    arg = parser.parse_args()

    main(arg.file_list)
