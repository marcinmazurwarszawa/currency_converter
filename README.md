# Currency Converter API

Z aplikacji wystawiony jest tylko 1 endpoint, który zwraca ilość przekonwertowanej waluty.<br>
W bazie danych cachowane są kursy pobrane z NBP na dany dzień (tak, żeby nie wysyłać za każdym razem requesta + żeby szybciej działało :D )<br>
W związku z tym, że program jest minimalnych rozmiarów wykorzystałem flaska i SQLAlchemy<br>
Postgree tylko dlatego, że SQLite nie obsługuje typu Decimal i SQLAlchemy rzutuje go na float<br>


# Instalacja

- git clone "repository" .
- dodać na poziomie app .env z następującymi parametrami:
```bash
POSTGRES_USER=mazi
POSTGRES_PASSWORD=mazi_password
POSTGRES_DB=currencies
DATABASE_URL=postgresql://mazi:mazi_password@db:5432/currencies
```
- stworzyć na poziomie app katalog dbdata
- odpalić program:
```bash
docker-compose up --build
```


# Odpalenie testów

```bash
docker-compose run app py.test
```


# Opis Endpointu

##### "/convert"  -  method GET
Należy przekazać następujące parametry:
- currency1: 3 literowy kod waluty z której przeliczamy<br>
- currency2: 3 literowy kod waluty na którą przeliczamy<br>
- amount: ilość przeliczanych pieniędzy

Przykładowy request:
- /convert?currency1=EUR&currency2=USD&amount=55

Przykładowa odpowiedź w formacie JSON:
- {"amount":"55","currency1":"EUR","currency2":"USD","value2":64.9889}
