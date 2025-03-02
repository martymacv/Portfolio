import json

from requests import Response


class Checking:
    """Методы для проверки ответов запросов"""
    def check_status_code(self, response: Response, expected_status_code: int):
        """Метод для проверки статус-кода"""
        assert expected_status_code == response.status_code
        if response.status_code == expected_status_code:
            print(f"Успешно!!! Статус код = {response.status_code}")
        else:
            print(f"Провал!!! Статус код = {response.status_code}")

    def check_json_data(self, response: Response, expected_values):
        """Метод для проверки наличия обязательных полей в ответе запроса"""
        assert sorted(response.json()) == sorted(expected_values)
        print(f"Все поля присутствуют")

    def check_json_value(self, response: Response, field_name, expected_values):
        """Метод для проверки значений обязательных полей в ответе запроса"""
        check = response.json()
        check_info = check[field_name]
        print(f"{field_name = } {check_info = }")
        assert check_info == expected_values
