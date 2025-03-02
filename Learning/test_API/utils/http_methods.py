import datetime

import requests
from logger import Logger


class HttpMethods:
    """Список HTTP методов"""
    headers = {'Content-Type': 'application/json'}
    cookie = ''
    logger = Logger(f"test_API/Logs/log_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log")

    @classmethod
    def get(cls, url):
        cls.logger.add_request(url, method='GET')
        result = requests.get(url=url, headers=cls.headers, cookies=cls.cookie)
        cls.logger.add_response(result)
        return result

    @classmethod
    def post(cls, url, body):
        cls.logger.add_request(url, method='POST')
        result = requests.post(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        cls.logger.add_response(result)
        return result

    @classmethod
    def put(cls, url, body):
        cls.logger.add_request(url, method='PUT')
        result = requests.put(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        cls.logger.add_response(result)
        return result

    @classmethod
    def delete(cls, url, body):
        cls.logger.add_request(url, method='DELETE')
        result = requests.delete(url=url, headers=cls.headers, cookies=cls.cookie, json=body)
        cls.logger.add_response(result)
        return result
