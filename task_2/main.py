from asyncio import AbstractEventLoop
from path import Path
import asyncio
import logging
import selectors

from app.file_worker import FileWorker
from app.site_parser import SiteParser
from app.utils import get_urls


async def main(loop: AbstractEventLoop) -> None:
    """High level логика парсера"""

    abspath = Path().abspath()
    save_folder = 'html'

    site_parser = SiteParser()
    file_worker = FileWorker(save_folder=save_folder, abspath=abspath)
    file_worker.create_folder(folder_name=save_folder)

    urls = get_urls(abspath=abspath)
    coroutines = [site_parser.get_source_code_from_url(url=url) for url in urls]
    iterator = asyncio.as_completed(coroutines)

    for get_source_code in iterator:

        try:
            # Не блокирующая функция. Вызываем в event_loop-е
            source_code = await get_source_code

        except Exception as e:
            logging.warning(e)

        else:
            # Блокирующая функция записи на диск. Запускаем ее в отдельном потоке
            loop.run_in_executor(None, file_worker.save_source_code, source_code)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Чтобы программа не завершалась с ошибкой
    selector = selectors.SelectSelector()
    event_loop = asyncio.SelectorEventLoop(selector)
    asyncio.set_event_loop(event_loop)

    event_loop.run_until_complete(main(loop=event_loop))
