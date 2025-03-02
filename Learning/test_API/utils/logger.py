import os
import datetime
from requests import Response


class Logger:
    def __init__(self, log_file_name: str):
        self.file_name = log_file_name
# print(file_name)
        #with open(self.file_name, 'w') as f:
         #   f.write('')

    def write_log_to_file(self, data: str):
        with open(self.file_name, 'a', encoding='utf-8') as log_f:
            log_f.write(data)

    def add_request(self, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"\n"
        self.write_log_to_file(data_to_add)

    def add_response(self, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)
        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"
        self.write_log_to_file(data_to_add)
