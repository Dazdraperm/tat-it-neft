from aiohttp import ClientSession

from .model import Site


class SiteParser:
    """Класс - парсер"""

    @staticmethod
    async def get_source_code_from_url(url: str) -> Site:
        """Скачиваем исходник HTML по url-у"""

        async with ClientSession() as session:
            async with session.get(url=url) as response:
                source_code = await response.read()
                host = response.host

        site = Site(
            host_name=host,
            source_code=source_code,
        )

        return site
