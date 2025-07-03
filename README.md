

# Zadanie rekrutacyjne Playwright

By uruchomić przedstawiony kod należy posiadać zainstalowanego playwrighta komendą ``` playwright install ``` oraz posiadać zainstalowane pakiety z pliku requirements.txt, mozna to zrobić używając komendy ```pip install -r requirements.txt```.

Posiadając niezbędne zależności można przystąpić do egzekucji testu przy użyciu komendy w terminalu :```pytest test_ing.py -n auto``` będąc w katalogu ```/TestING/tests```, bądź używając menu kontekstowego Playwrighta w VS Code.

Dodatkowo załączam mock prostego pipeline w Github Actions, niestety tylko mock, ponieważ przy próbie egzekucji, otrzymuję dodatkowy ekran z captcha (stąd też pojawia się conftest w celu zdebugowania kodu)

Screenshot: 
![Alt text](https://drive.google.com/u/0/drive-viewer/AKGpihad5-omXFAToNks5ygBqeuyESTdAotiE3xNKbqj9T_VZrZrLcZglUxkW0osBnVAB3dxMBbapLTUtj25fNws-W7d71_lk2YMwQ=s1600-rw-v1 "Wynik egzekucji github actions")
