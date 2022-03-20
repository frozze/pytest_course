from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest


class TestClassName(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_reg_1(self):
        browser = self.driver
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your first name")]')
        input1.send_keys("Pavel")
        input2 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your last name")]')
        input2.send_keys("Frost")
        input3 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your email")]')
        input3.send_keys("frozze@icloud.com")
        input4 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your phone:")]')
        input4.send_keys("+78125553535")
        input4 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your address:")]')
        input4.send_keys("SPB")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        # находим элемент, содержащий текст
        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text,
                         "Congratulations! You have successfully registered!", "Verified")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_reg_2(self):
        browser = self.driver
        browser.get("http://suninjuly.github.io/registration2.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your first name")]')
        input1.send_keys("Pavel")
        input2 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your last name")]')
        input2.send_keys("Frost")
        input3 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your email")]')
        input3.send_keys("frozze@icloud.com")
        input4 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your phone:")]')
        input4.send_keys("+78125553535")
        input4 = browser.find_element(By.XPATH, '//input[contains(@placeholder,"Input your address:")]')
        input4.send_keys("SPB")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text,
                         "Congratulations! You have successfully registered!", "Verified")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
    if __name__ == "__main__":
        unittest.main()
