import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ProjectUi import ProjectUi


@allure.title("Авторизация")
@allure.description("Указать логин и пароль")
@allure.feature("Auth")
@allure.severity("BLOCKER")
@pytest.mark.ui_test
def test_ui_auth():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    page_auth = ProjectUi(browser)
    with allure.step('Ввести логин'):
        page_auth.input_username()
    with allure.step('Ввести пароль'):
        page_auth.input_password()
    with allure.step('Нажать кнопку Войти'):
        page_auth.click_botton()
    with allure.step('Ждать загрузку страницы'):
        page_auth.wait_page()
    browser.quit()


@allure.title("Cоздать личное событие")
@allure.description("При создании обязательно указываем название")
@allure.feature("CreateEvent")
@allure.severity("MAJOR")
@pytest.mark.ui_test
def test_ui_add_event():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    add_event = ProjectUi(browser)
    with allure.step('Авторизация'):
        add_event.input_username()
        add_event.input_password()
        add_event.click_botton()
    with allure.step('Нажать на кнопку Плюс'):
        add_event.wait_add_event()
        add_event.click_add_plus()
    with allure.step('Нажать на кнопку Личное событие'):
        add_event.wait_personal_event()
        add_event.click_personal_event()
    with allure.step('Ввести название личного события'):
        add_event.input_personal_name("Дипломный проект, Савельев")
    with allure.step('Нажать на кнопку Добавить в расписание'):
        add_event.click_button_personal_event
    browser.quit()


@allure.title("Выключить набор")
@allure.description("При включенном наборе поступают заявки")
@allure.feature("Thumb")
@allure.severity("NORMAL")
@pytest.mark.ui_test
def test_ui_thumb():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    thumb = ProjectUi(browser)
    with allure.step('Авторизация'):
        thumb.input_username()
        thumb.input_password()
        thumb.click_botton()
    with allure.step('Нажать на тумблер'):
        bef = thumb.wait_week_calendar()
        af = thumb.click_thumb()
    with allure.step('Проверить, что тумблер работает'):
        assert bef != af
    browser.quit()


@allure.title("Вкл/выкл личное событие")
@allure.description("Вкл/выкл находятся в кнопке шестеренка")
@allure.feature("CogBtn")
@allure.severity("NORMAL")
@pytest.mark.ui_test
def test_ui_off_personal_event():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    cog_btn = ProjectUi(browser)
    with allure.step('Авторизация'):
        cog_btn.input_username()
        cog_btn.input_password()
        cog_btn.click_botton()
    with allure.step('Нажать на шестеренку'):
        bef = cog_btn.wait_week_calendar_for_off()
        cog_btn.click_cog_btn()
    with allure.step('Нажать на чекбокс'):
        cog_btn.click_checkbox()
        af = cog_btn.wait_week_calendar_for_off_two()
    with allure.step('Проверить количество событий после нажатия чекбокса'):
        assert bef != af
    browser.quit()


@allure.title("Переключение следующей недели")
@allure.description("Переключение по стрелочке")
@allure.feature("NewWeek")
@allure.severity("NORMAL")
@pytest.mark.ui_test
def test_ui_new_week():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    new_week = ProjectUi(browser)
    with allure.step('Авторизация'):
        new_week.input_username()
        new_week.input_password()
        new_week.click_botton()
    with allure.step('Нажать на стрелочку'):
        bef = new_week.wait_week_calendar_for_off_three()
        new_week.wait_chevron()
        af = new_week.wait_week_calendar_for_off_four()
    with allure.step('Проверить что неделя сменилась'):
        assert bef != af
    browser.quit()
