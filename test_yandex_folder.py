import requests
from class_Yandex_folder import YaUploader


class Test_yandex_create_folder:

    def setup(self):
        self.url = 'https://cloud-api.yandex.net/v1/disk/'
        self.url_folder_list = 'https://cloud-api.yandex.net/v1/disk/resources/'
        with open('ya_token.txt', 'r', encoding='utf-8') as file:
            ya_token = file.readline()
        self.ya_folder = YaUploader(ya_token)

    def teardown(self):
        print("method teardown")

    def test_yandex_status_code(self):
        response = requests.get(self.url, headers=self.ya_folder.get_headers()).status_code
        assert response == 200

    def test_yandex_response(self):
        assert self.ya_folder.ya_folder_create('Photo') == 404  # создается папка на яндекс-диске

    def test_yandex_list_folder(self):
        params = {
            "path": 'disk:/Photo'
        }
        response = requests.get(self.url_folder_list, headers=self.ya_folder.get_headers(), params=params).json()
        assert response["name"] == 'Photo'

    def test_yandex_status_code_negative(self):
        response = requests.get(self.url, headers=self.ya_folder.get_headers()).status_code
        assert response != 401
