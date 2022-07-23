import argparse
from typing import List
from yt_dlp import YoutubeDL
from loguru import logger


def log_file() -> None:
    logger.add("log/download_{time}.log", retention="30 days")


def read_list(file_path: str) -> List[str]:
    try:
        with open(file_path, encoding='UTF-8') as fp:
            return fp.readlines()
    except Exception as e:
        logger.error(e)
        return []


def write_list(url_list: List[str], file_path: str) -> bool:
    try:
        with open(file_path, 'w', encoding='UTF-8') as fp:
            fp.writelines(url_list)
        return True
    except Exception as e:
        logger.error(e)
        return False


SUCCESS_CODE = 0


def main(file_path: str):
    log_file()
    logger.info('Start download')
    logger.info(f'Read url list from :{file_path}')
    url_list = read_list(file_path)
    rest_url = []
    option = {'paths': {'home': 'nc'}}
    """
    if not download movie keep url to list.txt
    """
    if len(url_list) == 0:
        logger.warning('No Url List')
    with YoutubeDL(option) as ydl:
        for url in url_list:
            try:
                logger.info(f'Try {url} Download')
                return_code = ydl.download(url)
                if return_code != SUCCESS_CODE:
                    rest_url.append(url)
            except Exception as e:
                logger.exception(e)
                rest_url.append(url)

    write_list(rest_url, file_path)
    logger.info('Finish')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_list', default='list.txt', type=str)
    arg = parser.parse_args()

    main(arg.file_list)
