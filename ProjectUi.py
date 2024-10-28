from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProjectUi:
    """
    Класс Project показывает работу с сайтом.
    """

    def __init__(self, browser: str):
        """
        Специальная функция, которая вызывается при создании нового объекта
        класса. Запускает страницу Chrome на полное окно с ожиданием 4 сек.
        """
        self._driver = browser
        self._driver.get("https://teachers.skyeng.ru")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def input_username(self):
        """Ввести логин"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="username"]'))
        )
        input_username = self._driver.find_element(
            By.CSS_SELECTOR, '[name="username"]')
        input_username.clear()
        input_username.send_keys("test.tst345@skyeng.ru")

    def input_password(self):
        """Ввести пароль"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="password"]'))
        )
        input_password = self._driver.find_element(
            By.CSS_SELECTOR, '[name="password"]')
        input_password.clear()
        input_password.send_keys("2DbhAAPG6q")

    def wait_page(self):
        """Ждать загрузки сайта"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.week-calendar")
            )
        )

    def click_botton(self):
        """Нажать кнопку Войти"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.button.button--primary'))
        )
        click_botton = self._driver.find_element(
            By.CSS_SELECTOR, ".button.button--primary"
        )
        click_botton.click()

    def wait_add_event(self):
        """Ждать загрузку кнопки Плюс"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-icon"))
        )

    def click_add_plus(self):
        """Нажать на кнопку Плюс"""
        self._driver.find_element(By.CSS_SELECTOR, ".add-icon").click()

    def wait_personal_event(self):
        """Ждать загрузки кнопки Личное событие"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 'span[class="text-center text-ellipsis width-100"]')
            )
        )

    def click_personal_event(self):
        """Нажать на кнопку Личное событие"""
        click_add_event = self._driver.find_element(
            By.XPATH,
            '//*[@id="cdk-overlay-0"]/cabinet-schedule-class-slot-modal/sky-ui-popup/div/div/div[2]/div/div[1]/div/sky-ui-tabs/div/sky-ui-tab[2]/div/span',
        )
        click_add_event.click()

    def input_personal_name(self, my_name: str):
        """Вести данные в поле"""
        input_name = self._driver.find_element(
            By.XPATH,
            '//*[@id="cdk-overlay-0"]/cabinet-schedule-class-slot-modal/sky-ui-popup/div/div/div[2]/div/div[2]/cabinet-schedule-personal-event-form/div/div[1]/input',
        )
        input_name.clear()
        input_name.send_keys(my_name)

    def click_button_personal_event(self):
        """Нажать кнопку Сохранить"""
        click_add = self._driver.find_element(
            By.CSS_SELECTOR,
            'button[class="root -type-primary -color-brand -size-m -active"]',
        )
        click_add.click()

    def wait_week_calendar(self):
        """Ждать загрузки кнопки Личное событие"""
        before_thumb = self._driver.find_element(
            By.CSS_SELECTOR, "div.is-accepting-new-students"
        ).text
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.week-calendar"))
        )
        return before_thumb

    def click_thumb(self):
        """Нажать на тумблер"""
        self._driver.find_element(By.CSS_SELECTOR, "div.thumb").click()
        after_thumb = self._driver.find_element(
            By.CSS_SELECTOR, "div.is-accepting-new-students"
        ).text
        return after_thumb

    def wait_week_calendar_for_off(self):
        """Ждать загрузки Календаря"""
        before_events = self._driver.find_elements(
            By.CSS_SELECTOR, "tcc-calendar-event"
        )
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.week-calendar"))
        )
        return len(before_events)

    def click_cog_btn(self):
        """Нажать на шестеренку"""
        self._driver.find_element(By.CSS_SELECTOR, "button.cog-btn").click()

    def wait_page_cog_btn(self):
        """Ждать загрузки чекбокса"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.checkbox"))
        )

    def click_checkbox(self):
        """Нажать на тумблер"""
        self._driver.find_element(By.CSS_SELECTOR, "div.checkbox").click()

    def wait_week_calendar_for_off_two(self):
        """Ждать загрузки Календаря"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.week-calendar"))
        )
        after_events = self._driver.find_elements(
            By.CSS_SELECTOR, "tcc-calendar-event")
        return len(after_events)

    def wait_week_calendar_for_off_three(self):
        """Ждать загрузки Календаря"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.week-calendar"))
        )
        before_week = self._driver.find_element(
            By.CSS_SELECTOR, "div.week-filter.font-open-sans"
        ).text
        return before_week

    def wait_chevron(self):
        """Ждать загрузки Стрелки"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'svg[data-icon="chevron-right"]')
            )
        ).click()

    def wait_week_calendar_for_off_four(self):
        """Ждать загрузки Календаря"""
        WebDriverWait(self._driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.week-calendar"))
        )
        after_week = self._driver.find_element(
            By.CSS_SELECTOR, "div.week-filter.font-open-sans"
        ).text
        return after_week
