import requests
def QCC():
    print('Welcome to Quick Currency Calculator')
    waluta = input('Wprowadź kod waluty zagranicznej (KKK): ')
    waluta = waluta.upper()
    data = input('Wprowadź datę do pobrania kursu (RRRR-MM-DD): ')
    zapytanie = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data}/?format=json")
    #{"table":"A",
    # "currency":"dolar amerykański",
    # "code":"USD",
    # "rates":[{"no":"193/A/NBP/2022",
    #       "effectiveDate":"2022-10-05",
    #       "mid":4.8380}]}
    dane = zapytanie.json()
    kurs = dane["rates"][0]["mid"]

    print(f"1 PLN = {kurs} {waluta}")
    if kurs:
        print('Success!')
    else:
        print('Error!')

    ##Przeliczanie konkretnej, zadanej kwoty
    kwota_pln = input('Wprowadź kwotę w PLN: ')
    kwota_pln = float(kwota_pln)
    kwota_przeliczona = kwota_pln * kurs
    print(f"{kwota_pln} PLN = {kwota_przeliczona} {waluta}")

QCC()
