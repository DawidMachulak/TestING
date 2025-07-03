

# Zadanie rekrutacyjne Playwright

By uruchomić przedstawiony kod należy posiadać zainstalowanego playwrighta komendą ``` playwright install ``` oraz posiadać zainstalowane pakiety z pliku requirements.txt, mozna to zrobić po wcześniejszym stworzeniu venva używając komendy ```pip install -r requirements.txt```.

Posiadając niezbędne zależności można przystąpić do egzekucji testu przy użyciu komendy w terminalu :```pytest test_ing.py -n auto``` będąc w katalogu ```/TestING/tests```, bądź używając menu kontekstowego Playwrighta w VS Code.

Dodatkowo załączam mock prostego pipeline w Github Actions pod ścieżką ```TestING/mock/.github/workflows```, niestety tylko mock, ponieważ przy próbie egzekucji, otrzymuję dodatkowy ekran z captcha (stąd też pojawia się conftest w celu zdebugowania kodu)

Screenshot: 
![image](https://drive.google.com/uc?export=view&id=1pz1lbzyKxpzd8a33h1BWN2GPIpzyGv2k)
