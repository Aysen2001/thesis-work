import requests


class ProjectApi:
    def __init__(self, api: str, global_token: str):
        self.api = api
        self.header = {"cookie": global_token}

    def create_event(self, prod_data: str):
        """Создать личное событие"""
        responce = requests.post(
            self.api + "/createPersonal", data=prod_data, headers=self.header
        )
        return responce.status_code

    def update_event(self, prod_data: str):
        """Изменить личное событие"""
        responce = requests.post(
            self.api + "/updatePersonal", data=prod_data, headers=self.header
        )
        return responce.status_code

    def remove_event(self, prod_data: str):
        """Удалить личное событие"""
        responce = requests.post(
            self.api + "/removePersonal", data=prod_data, headers=self.header
        )
        return responce.status_code

    def move_class(self, prod_data: str):
        """Перенести урок"""
        responce = requests.post(
            self.api + "/moveClass", data=prod_data, headers=self.header
            )
        return responce.status_code

    def rooms(self):
        """Перейти в комнату урока"""
        self.api = "https://api-english.skyeng.ru/api/v2"
        responce = requests.get(
            self.api + "/rooms/xivonoxasize", headers=self.header)
        return responce.status_code
