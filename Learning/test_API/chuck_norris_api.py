import requests


class Request:
    """Обвязка для requests"""

    def __init__(self, url):
        """При инициализации класса делаем GET-запрос"""
        self.__response = requests.get(url)

    @property
    def joke_category(self):
        return set(self.__response.json()['categories'])

    @property
    def joke(self):
        """Геттер для шутки про Чака с проверкой на пустую строку"""
        assert type(self.__response.json().get('value', None)) == str, 'joke is exist or not string'
        return self.__response.json().get('value', None)

    @property
    def json_data(self):
        """Геттер для получения данных ответа в формате json"""
        return self.__response.json()

    @property
    def status_code(self):
        """Геттер для получения статус кода ответа"""
        return self.__response.status_code


class TestRequest(Request):
    """Тесты"""

    def __init__(self, url):
        super().__init__(url)

    def test_status_code(self):
        """Тест статус кода"""
        print('status code'.rjust(20), f'is {self.status_code}')
        assert 200 == self.status_code

    def test_chuck_joke(self):
        """Проверка принадлежности шутки к Чаку"""
        print('is about chuck?'.rjust(20), ('NO', 'YES')['Chuck' in self.joke])
        assert 'Chuck' in self.joke

    def test_joke_category(self, joke_categories: list):
        """Проверка категории шуток"""
        print('category not exist?'.rjust(20), ('NO', 'YES')[self.joke_category.issubset(set(joke_categories))])
        assert self.joke_category.issubset(set(joke_categories))

    def __str__(self):
        """Информационное сообщение об объекте тестирования"""
        return f"{'joke':>20} {self.joke}"


if __name__ == '__main__':
    joke_categories = Request(f"https://api.chucknorris.io/jokes/categories").json_data
    print(f"{joke_categories = }")
    joke_category = TestRequest(f"https://api.chucknorris.io/jokes/random?category={input('Введите категорию шуток: ')}")
    print(joke_category)
    joke_category.test_status_code()
    joke_category.test_joke_category(joke_categories)

    # joke_per_category = [TestRequest(f"https://api.chucknorris.io/jokes/random?category={category}")
    #                      for category in joke_categories]
    # test_result_per_joke = [(test.print_joke(), test.test_status_code(), test.test_joke())
    #                         for test in joke_per_category]
