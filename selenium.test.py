import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep
from faker import Faker

class RegistrationTests(unittest.TestCase):
    def setUp(self):
        """Test preparation"""
        self.fake = Faker("pl_Pl")
        # Przygotowanie testu
        # 1. Otwarta strona główna
        # 1a) Tworzę instancję klasy Chrome()
        self.driver = webdriver.Chrome()
        # (Zmaksymalizuj okno)
        self.driver.maximize_window()
        # 1b) Otwieram stronę główną
        self.driver.get("https://www.eobuwie.com.pl/")
        cookie_accept = self.driver.find_element(By.XPATH, '//div[@class="e-consents-alert__actions"]/button[1]')
        cookie_accept.click()
        sleep(3)

    def tearDown(self):
        # Wyłącz przeglądarkę
        self.driver.quit()

    def testNoNameEntered(self):
        # KROKI
        # 1. Kliknij „Zarejestruj”
        # 1a) Odszukaj przycisk Zarejestruj
        # 1b) Kliknij ten przycisk
        zarejestruj_a = self.driver.find_element(By.XPATH, '//a[@data-testid="header-register-link"]')
        zarejestruj_a.click()
        # 2. Wpisz nazwisko
        # Odszukaj, wpisz
        nazwisko_input = self.driver.find_element(By.ID, "lastname")
        nazwisko_input.send_keys(self.fake.last_name())
        # 3. Wpisz adres e-mail
        email_address_input = self.driver.find_element(By.ID, "email_address")
        email_address_input.send_keys(self.fake.email())
        # 4. Wpisz hasło
        password_input = self.driver.find_element(By.ID, "password")
        password = self.fake.password()
        password_input.send_keys(password)
        # 5. Potwierdź hasło
        conf_input = self.driver.find_element(By.ID, "confirmation")
        conf_input.send_keys(password)
        # 6. Akceptuj regulamin
        self.driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label"]').click()
        # (OSTROŻNIE!) 7. Kliknij Załóż konto, żeby wywołać informację o błędzie
        create_btn = self.driver.find_element(By.ID, "create-account")
        create_btn.click()
        sleep(4)
        # UWAGA! TU BĘDZIE TEST!
        # OCZEKIWANY REZULTAT
        # a) Szukam wszystkich elementów (informacji o błędzie użytkownika)
        errors = self.driver.find_elements(By.XPATH, '//span[@class="form-error"]')
        # b) Sprawdzam, czy jest tylko jeden taki element
        self.assertEqual(1, len(errors))
        # c) Sprawdzam poprawność treści tego komunikatu i jego widoczność
        self.assertEqual("To pole jest wymagane", errors[0].text)
        # d) Sprawdzam, czy komunikat jest pod polem imię (i nad innymi polami)
        imie_input = self.driver.find_element(By.ID, "firstname")
        errors2 = self.driver.find_elements(locate_with(By.XPATH, '//span[@class="form-error"]').near(imie_input))
        # e) Sprawdzam, czy element zawarty wewnątrz listy errors oraz errors2, to ten sam element
        self.assertEqual(errors[0].id, errors2[0].id)
        sleep(2)