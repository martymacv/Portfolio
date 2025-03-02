import json
import requests


class Request:
    """Обвязка для requests"""

    def __init__(self, base_url: str):
        self.__base_url = base_url
        self.__response = None

    def get_response(self):
        """Геттер для получения объекта типа Response"""
        return self.__response

    def set_response(self, response):
        """Сеттер для сохранения объекта типа Response"""
        self.__response = response

    response = property(get_response, set_response)

    @property
    def response_content(self):
        """Геттер для получения данных в формате json"""
        return self.__response.json()

    @property
    def base_url(self):
        """Геттер для получения урла"""
        return self.__base_url

    @property
    def status_code(self):
        """Геттер для получения статус кода ответа"""
        return self.__response.status_code


class PostRequest(Request):
    """Класс с реализацией сборки POST запроса"""

    def __init__(self, base_url: str, resource: str, params: dict, body: dict):
        super().__init__(base_url)
        self.__resource = resource
        self.__params = dict(params)
        self.__body = dict(body)

    def post_request(self):
        """Сборка POST запроса, отправка и сохранение ответа"""
        params = '&'.join([f"{key}={value}" for key, value in self.__params.items()])
        url = f"{self.base_url}{self.__resource}?{params}"
        body = self.__body
        print(f"send url: {url}")
        print(f"with params: {json.dumps(self.__params)}")
        print(f"with body: {json.dumps(body)}")
        self.response = requests.post(url=url, json=body)
        # Проверки статусов
        print(f"status code: {self.status_code}")
        assert 200 == self.status_code, f"error: {self.status_code} {self.response_content}"
        print(f"status: {self.response.json()['status']}")
        assert 'OK' == self.response.json()['status']


class DelRequest(Request):
    """Класс с реализацией сборки DELETE запроса"""

    def __init__(self, base_url: str, resource: str, params: dict, body: dict):
        super().__init__(base_url)
        self.__resource = resource
        self.__params = dict(params)
        self.__body = dict(body)

    def del_request(self):
        """Сборка DELETE запроса, отправка и сохранение ответа"""
        params = '&'.join([f"{key}={value}" for key, value in self.__params.items()])
        url = f"{self.base_url}{self.__resource}?{params}"
        print(f"send url: {url}")
        print(f"with params: {json.dumps(self.__params)}")
        print(f"with body: {json.dumps(self.__body)}")
        self.response = requests.delete(url=url, json=self.__body)
        # Проверки статусов
        print(f"status code: {self.status_code}")
        if self.status_code == 200:
            assert 200 == self.status_code
        elif self.status_code == 404:
            assert 404 == self.status_code
        print(f"status: {self.response.content}")
        # assert 'OK' == self.response.json()['status']
        # print(f"massage: {self.response.json()['msg']}")


class GetRequest(Request):
    """Класс с реализацией сборки GET запроса"""

    def __init__(self, base_url: str, resource: str, params: dict):
        super().__init__(base_url)
        self.__resource = resource
        self.__params = dict(params)

    def get_request(self):
        """Сборка GET запроса, отправка и сохранение ответа"""
        params = '&'.join([f"{key}={value}" for key, value in self.__params.items()])
        url = f"{self.base_url}{self.__resource}?{params}"
        print(f"send url: {url}")
        print(f"with params: {json.dumps(self.__params)}")
        self.response = requests.post(url=url)
        print(f"status code: {self.status_code}")
        if self.status_code == 200:
            assert 200 == self.status_code
        elif self.status_code == 404:
            assert 404 == self.status_code
        print(f"response content: {self.response.json()}")

    @property
    def params(self):
        """Геттер для получения списка параметров в формате dict"""
        return self.__params

    def add_params(self, params: dict):
        """Обогащение параметров для запроса (базовый параметр + произвольный набор)"""
        self.__params.update(params)
        print(f"request params: {json.dumps(self.__params)} has been update successfully")


class GoogleMapAPI:
    """Класс тестируемой системы"""

    def __init__(self):
        """Инициализация класса с базовыми атрибутами для работы с API"""
        self.base_url = "https://rahulshettyacademy.com"
        self.get_resource = "/maps/api/place/get/json"
        self.post_resource = "/maps/api/place/add/json"
        self.put_resource = ""
        self.delete_resource = "/maps/api/place/delete/json"
        self.base_params = {
            "key": "qaclick123"
        }
        self.body_to_post = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        self.__bodies_to_delete = []
        self.__place_id = set()

    @property
    def bodies_to_delete(self):
        return self.__bodies_to_delete

    def add_place_id(self, place_id: str):
        """Сохранение place_id в json-файл (для удобства)"""
        with open('place_id_list.json', 'w', encoding='utf-8') as json_out:
            self.__place_id.add(place_id)
            json.dump([{"place_id": place} for place in list(self.__place_id)], json_out, indent=4)
        with open('place_id_list1.json', 'w', encoding='utf-8') as json_out:
            self.__place_id.add(place_id)
            json.dump([{"place_id": place} for place in list(self.__place_id)], json_out, indent=4)
        print(f"new place_id: {place_id} has been save successfully")
        with open('place_id_list.json', 'r', encoding='utf-8') as json_in:
            # проверка, что place_id действительно добавился в файл
            assert place_id in list(map(lambda x: x['place_id'], json.load(json_in)))

    def del_place_id(self, place_id: dict):
        """Удаляем place_id из json-файла"""
        with open('place_id_list.json', 'r', encoding='utf-8') as json_r:
            place_id_list = json.load(json_r)
            # проверка, что place_id действительно есть в файле
            assert place_id in place_id_list
            with open('place_id_list.json', 'w', encoding='utf-8') as json_w:
                place_id_list.remove(place_id)
                json.dump(place_id_list, json_w, indent=4)
            # проверка, что place_id действительно удален из файла
            assert place_id not in place_id_list
        print(f"place_id: {place_id['place_id']} has been delete successfully")
        self.__place_id.remove(place_id['place_id'])
        self.__bodies_to_delete.append(place_id)


if __name__ == '__main__':
    # создаем объект тестирования
    test_obj = GoogleMapAPI()

    print("\nсоздаем сборки post-запросов")
    post_requests = [PostRequest(base_url=test_obj.base_url,
                                 resource=test_obj.post_resource,
                                 params=test_obj.base_params,
                                 body=test_obj.body_to_post)
                     for _ in range(5)]
    print("\nдобавляем новые локации в GoogleMap")
    for post_request in post_requests:
        post_request.post_request()
        test_obj.add_place_id(post_request.response.json()['place_id'])
    with open('place_id_list.json', encoding='utf-8') as json_f:
        places = json.load(json_f)
        print("\nсоздаем сборки get-запросов")
        get_requests = [GetRequest(base_url=test_obj.base_url,
                                   resource=test_obj.get_resource,
                                   params=test_obj.base_params)
                        for place_id in places]
        print("\nобогащаем get-запросы параметром place_id")
        [get_request.add_params(place_id) for get_request, place_id in zip(get_requests, places)]
        print("\nпроверяем, что новые локации действительно созданы")
        [get_request.get_request() for get_request in get_requests]

    print("\nготовим список локаций к удалению из GoogleMap")
    [test_obj.del_place_id(place_id) for place_id in places[1::2]]
    print("\nсоздаем сборки delete-запросов")
    del_requests = [DelRequest(base_url=test_obj.base_url,
                               resource=test_obj.delete_resource,
                               params=test_obj.base_params,
                               body=body_to_delete)
                    for body_to_delete in test_obj.bodies_to_delete]
    print("\nудаляем локации из GoogleMap по списку")
    [del_request.del_request() for del_request in del_requests]
    print("\nпроверяем, что локации из списка действительно удалены")
    [get_request.get_request()
     for get_request in list(filter(lambda x: x.params['place_id'] in list(map(lambda y: y['place_id'],
                                                                               test_obj.bodies_to_delete)),
                                    get_requests))]
    print("\nповторно удаляем локации из GoogleMap по списку")
    [del_request.del_request() for del_request in del_requests]
