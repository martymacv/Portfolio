from http_methods import HttpMethods


class GoogleMapsAPI(HttpMethods):
    """Методы для тестирования Google Maps API"""

    def __init__(self):
        self.base_url = "https://rahulshettyacademy.com"
        self.get_resource = "/maps/api/place/get/json"
        self.post_resource = "/maps/api/place/add/json"
        self.put_resource = "/maps/api/place/update/json"
        self.delete_resource = "/maps/api/place/delete/json"
        self.params = {"key": "qaclick123"}
        self.json_for_create_new_place = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [(pyTest) PS C:\Users\Всеволод\IdeaProjects\pyTest> py .\my_program.py
Чек № 1
Покупатель: Иван Иванов Иванович
Дата: 12.12.2020
Время: 12:00
Итого: 100
Молоко 50 2
Хлеб 30 1
Чек № 2
Покупатель: Петр Петров Петрович
Дата: 12.12.2020
Время: 12:00
Итого: 100
Молоко 50 2
Хлеб 30 1

                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }
        self.json_for_update_new_location = {
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        self.json_for_delete_new_location = dict()

    def create_new_place(self):
        """Метод для создания новой локации"""
        params = '&'.join([f"{key}={value}" for key, value in self.params.items()])
        post_url = f"{self.base_url}{self.post_resource}?{params}"
        print(post_url)
        result_post = self.post(url=post_url, body=self.json_for_create_new_place)
        print(result_post.text)
        return result_post

    def get_new_place(self, place_id):
        """Метод для проверки новой локации"""
        params = self.params
        params.update({"place_id": place_id})
        params = '&'.join([f"{key}={value}" for key, value in params.items()])
        get_url = f"{self.base_url}{self.get_resource}?{params}"
        print(get_url)
        result_get = self.get(get_url)
        print(result_get.text)
        return result_get

    def put_new_place(self, place_id):
        """Метод для изменения новой локации"""
        put_url = f"{self.base_url}{self.put_resource}"
        print(put_url)
        body = self.json_for_update_new_location
        body.update({"place_id": place_id})
        result_put = self.put(url=put_url, body=body)
        print(result_put.text)
        return result_put

    def delete_new_place(self, place_id):
        """Метод для удаления новой локации"""
        delete_url = f"{self.base_url}{self.delete_resource}"
        print(delete_url)
        body = self.json_for_delete_new_location
        body.update({"place_id": place_id})
        result_delete = self.delete(url=delete_url, body=body)
        print(result_delete.text)
        return result_delete
