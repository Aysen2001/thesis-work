import allure
import pytest
from ProjectApi import ProjectApi

api = "https://api-teachers.skyeng.ru/v2/schedule"
#  Введите актуальный токен
global_token = 'token_global=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjE0ODk0MjUwLCJpZGVudGl0eSI6InRlc3QudHN0MzQ1QHNreWVuZy5ydSIsImlkZW50aXR5TG9naW4iOm51bGwsImlkZW50aXR5RW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJpZGVudGl0eVBob25lIjoiKzc5MTY1MDAyMjU1IiwibmFtZSI6Ilx1MDQxMFx1MDQzYlx1MDQzNVx1MDQzYVx1MDQ0MVx1MDQzNVx1MDQzOSIsInN1cm5hbWUiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0LnRzdDM0NUBza3llbmcucnUiLCJ1aUxhbmd1YWdlIjoicnUiLCJsb2NhbGUiOiJydSIsInNlcnZpY2VMb2NhbGUiOm51bGwsInVhcyI6MzAsImp3dFR5cGUiOjEsImp0aSI6InhualZTS3o5ZXloR1VBSE5WRnJKSWpjSFlDYXFTVHFIIiwiYnJhbmQiOm51bGwsImV4cCI6MTczMDEyMzEzOSwiYmlydGhkYXkiOiIyMDA2LTEwLTEwIiwiYUlzU3Ryb25nIjp0cnVlLCJhVHlwZSI6IlVTRVJOQU1FX1BBU1NXT1JEIiwiYVRpbWUiOjE3Mjk4NzExMzQsInJvbGVzIjpbIlJPTEVfVEVBQ0hFUl9DQU5ESURBVEUiLCJST0xFX1RFQUNIRVJfQ0FORElEQVRFX0JBU0VfQUNDRVNTIiwiUk9MRV9UVENfVVNBR0UiLCJST0xFX1ZJTUJPWF9URUFDSEVSX1VTQUdFIiwiUk9MRV9URUFDSEVSIiwiUk9MRV9DUk0yX1RFQUNIRVJfQUNDRVNTIiwiUk9MRV9NQVRIX1RFQUNIRVIiLCJST0xFX01BVEhfQ09OVEVOVF9USEVNRV9WSUVXIl19.kO7LM-txk8xCTxqTMItSDja27CKgwqccKLlz_KF2XC0o0OqupbqBACeJq9jVW1vdZnRP9_B3gyaUUuW4zF0iWe5y3jnRtWmQLsMkWZqUNpn3jhjFu4Oe6SSL8zLcKSa2MiPsHI_TF52cFi9hyMshqd8HpUdYDnIb1oT0-KJQS-B7z-i6fNNn5pjEBmPoKrxQgtAqGzfRJ09uLxdPd9n9LvisS0HY7iNP3aveeZIqRISOVNVgs9qq5yOAyDrYnKxQOODrbbiQaeX3nORUYeA3WQTgUbQ_oM03zaxroLQjBDpbty12x2jRaAb8YbcEoR9lYO9dAK-K7ZVJImgg6ZS91wBFt4A7siVN4OZjF2d_bmK0yl33vFwBdmQbJM4kHanMZeJU7S4LYAaSbftDR8PSMNJCrCBUQ4gh9OThsJ5bDHbV_L8NpNuSrokScdimUj9YPRj4Z3EaKYCZeBfD52t2TIkiMRv75WFyRDi-yQcIYGa4HJwkQ4F5fLjQT4G425QXNQ0bNvhcj59SCjCq1xxp37arsO-syhFjTyuW_srS4vtwcvulQ-pPpx8BBYU4WTJ8rVxgT7SpL3a9sFcONOVCeNYMfluZ-ZV3YqI4R6ozhvaWxvb7tgdyf-gqsH6isFVRQ_V3V2ggDJI9a0-LV8LenW8RJGBxL9ClelFpXbyWXjc'


@allure.title("Cоздать личное событие")
@allure.description("При создании обязательно указываем название")
@allure.feature("CreateEvent")
@allure.severity("MAJOR")
@pytest.mark.api_test
def test_create_event():
    event = ProjectApi(api, global_token)
    prod_data = {
        "backgroundColor": "#F4F5F6",
        "color": "#81888D",
        "description": "",
        "title": "Новое событие",
        "startAt": "2024-10-25T17:30:00+04:00",
        "endAt": "2024-10-25T18:00:00+04:00"
        }
    with allure.step('Создание нового личного события'):
        responce = event.create_event(prod_data)
    with allure.step('Проверка кода состояния ответа'):
        assert responce == 200


@allure.title("Изменить личное событие")
@allure.description(
    "При изменение указываем id, и меняем параметр")
@allure.feature("UpdateEvent")
@allure.severity("MAJOR")
@pytest.mark.api_test
def test_update_event():
    event = ProjectApi(api, global_token)
    prod_data = {
        "backgroundColor": "#F4F5F6",
        "color": "#81888D",
        "description": "",
        "title": "Обновленное событие",
        "startAt": "2024-10-25T17:30:00+04:00",
        "endAt": "2024-10-25T18:00:00+04:00",
        "id": 99789127,
        "oldStartAt": "2024-10-25T17:30:00+04:00"
        }
    with allure.step('Изменение личного события'):
        responce = event.update_event(prod_data)
    with allure.step('Проверка кода состояния ответа'):
        assert responce == 200


@allure.title("Удалить личное событие")
@allure.description("При удалении обязательно указываем id")
@allure.feature("RemoveEvent")
@allure.severity("MAJOR")
@pytest.mark.api_test
def test_remove_event():
    event = ProjectApi(api, global_token)
    prod_data = {
        "id": 99789127,
        "startAt": "2024-10-25T17:30:00+04:00"
        }
    with allure.step('Удаление личного события'):
        responce = event.remove_event(prod_data)
    with allure.step('Проверка кода состояния ответа'):
        assert responce == 200


@allure.title("Перенос урока")
@allure.description("Указываем причины переноса")
@allure.feature("MoveClass")
@allure.severity("NORMAL")
@pytest.mark.api_test
def test_moveClass():
    event = ProjectApi(api, global_token)
    prod_data = {
        "virtualClassId": "R6935147-1730048400",
        "newStartAt": "2024-10-28T21:00:00+04:00",
        "initiator": 1,  # инициатор
        "reason": 6,  # причина
        "comment": "Болезнь",
        "isMoveRegular": False
        }
    with allure.step('Перенос урока'):
        responce = event.move_class(prod_data)
    with allure.step('Проверка кода состояния ответа'):
        assert responce == 200


@allure.title("Вход в комнату урока")
@allure.description("")
@allure.feature("Room")
@allure.severity("NORMAL")
@pytest.mark.api_test
def test_rooms():
    event = ProjectApi(api, global_token)
    with allure.step('Вход в комнату урока'):
        responce = event.rooms()
    with allure.step('Проверка кода состояния ответа'):
        assert responce == 200
