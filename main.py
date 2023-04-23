import unittest
from selenium import webdriver

class RegistrationtTest(unittest.TestCase):
    def setUp(self):
        #Przygotowanie testu (warunki wstępne)
        #1.Otwarta strona główna
        #1a.Tworzę instancję klasy Chrome() czyli obiekt
        self.driver = webdriver.Chrome()
        #(Zmaksymalizuj okno)
        self.driver.maximize_window()
        #1b.Otwieram stronę główną
        self.driver.get("https://www.eobuwie.com.pl/")

    def testNoNameEntered(self):
        #KROKI
        #1.Kliknij "Zarejestruj"
        #1a.Odszukaj przycisk Zarejestruj
        #1b.Kliknij ten przycisk
        pass
