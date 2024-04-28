#!/usr/bin/env python3

from bs4 import BeautifulSoup
import aiohttp
import asyncio

async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.find_all('a') if a.has_attr('href')]

async def get_all_links(urls):
    tasks = [get_html(url) for url in urls]
    return await asyncio.gather(*tasks)

async def main():

    pass

if __name__ == '__main__':
    main()