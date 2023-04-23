def dodaj_advanced(*args):
    wynik = 0
    for arg in args:
        wynik = wynik + arg
    return wynik

def funkcja(**kwargs):
    print(type(kwargs))
    print(kwargs)