import sys
sys.path.extend(("C:\\Users\\Всеволод\\PycharmProjects\\Portfolio\\Learning\\test_API\\utils",))

import allure

from requests import Response
from api import GoogleMapsAPI
from checking import Checking


class TestCreatePlace:
    """Создание, изменение и удаление новой локации"""
    google_maps_api = GoogleMapsAPI()
    check_list = Checking()

    @classmethod
    def test_create_new_place(cls):
        print("Метод POST")
        result_post: Response = cls.google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        cls.check_list.check_status_code(result_post, 200)
        cls.check_list.check_json_data(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        cls.check_list.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get: Response = cls.google_maps_api.get_new_place(place_id)
        cls.check_list.check_status_code(result_get, 200)
        cls.check_list.check_json_data(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        cls.check_list.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Метод PUT")
        result_put: Response = cls.google_maps_api.put_new_place(place_id)
        cls.check_list.check_status_code(result_put, 200)
        cls.check_list.check_json_data(result_put, ['msg'])
        cls.check_list.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get: Response = cls.google_maps_api.get_new_place(place_id)
        cls.check_list.check_status_code(result_get, 200)
        cls.check_list.check_json_data(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        cls.check_list.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Метод DELETE")
        result_delete: Response = cls.google_maps_api.delete_new_place(place_id)
        cls.check_list.check_status_code(result_delete, 200)
        cls.check_list.check_json_data(result_delete, ['status'])
        cls.check_list.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get: Response = cls.google_maps_api.get_new_place(place_id)
        cls.check_list.check_status_code(result_get, 404)
        cls.check_list.check_json_data(result_get, ['msg'])
        cls.check_list.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("Тестирование создания, изменения и удаления новой локации прошло успешно!!!")
