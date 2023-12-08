import aiohttp
from typing import Dict, Optional
import json
from config_reader import config


async def call_creator(telegram_id: int, username: str) -> Optional[Dict[str, int]]:
    API_URL = "http://127.0.0.1:8000/creator/"
    data = {'telegram_id': telegram_id, 'username': username}

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json=data) as response:
            if response.status == 201:
                result = await response.json()
                print(result)
                return result
            else:
                return None


async def upload_quiz(file_path: str, telegram_id: int) -> bool:
    API_URL = "http://127.0.0.1:8000/4/uploadquiz/"
    token = config.token_api.get_secret_value()
    file_url = f'https://api.telegram.org/file/bot{token}/{file_path}'


    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as resp:
            if resp.status == 200:
                file_data = await resp.read()

                # Подготовка данных для отправки
                form = aiohttp.FormData()
                form.add_field('docx_file', file_data, filename='document.docx')
                form.add_field('telegram_id', str(telegram_id))

                async with session.post(API_URL, data=form) as response:
                    if response.status == 201:
                        return True
            return False
async def quiz_list():
    pass