import requests
def QCC():
    print('Welcome to Quick Currency Calculator')
    waluta = input('Please enter any currency code (CCC): ')
    waluta = waluta.upper()
    data = input('Please enter date of for exchange rates (YYYY-MM-DD): ')
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
    kwota_pln = input('Please enter the amount in PLN to be converted: ')
    kwota_pln = float(kwota_pln)
    kwota_przeliczona = kwota_pln / kurs
    kwota_przeliczona = round(kwota_przeliczona, 2)
    print(f"{kwota_pln} PLN = {kwota_przeliczona} {waluta}")
    print('Thank you for using QCC!' )
QCC()
