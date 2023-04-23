import unittest

class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu (Warunki wstepne)")

    def testPierwszy(self):
        #zaczyna się od slowa "test"
        print("Test(kroki)")
        wynik_oczekiwany = 5
        wynik_rzeczywisty = 5
        self.assertEqual(wynik_oczekiwany, wynik_rzeczywisty)

    def testDrugi(self):
        print("Test drugi")

    def tearDown(self):
        print("Sprzatanie po teście")

#sprawdzam, czy ten moduł jest modułem głównym
#(Czy uruchomiono cały projekt z tego pliku)
if __name__ == "__main__":
    unittest.main()