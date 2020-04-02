# Lesson 03 - Funktionen & Module

## Funktionen
1. Wie könnte eine Funktion aussehen, die Nutzer namentlich begrüßt?
    ```python
        def greetUsers(names):
            for name in names:
                print("Hallo "+name)

        def greetUser(name):
            print("Hallo "+name)
    ```
2. Warum benutzt man Funktionen?
    - Code übersichtlicher
    - Weniger Code (oft benutzte elemente können abgekürzt werden)

## Module
1. Gib das aktuelle Datum in die Konsole aus (datetime-modul)
    ```python
        from datetime import datetime
        print(datetime.today())
    ```
2. Wie erhält man 'Web-Content' von z.B.: [Website von Spiegel Online](https://www.spiegel.de/)?
    ```python
        import requests
        response = requests.get(url)
        content = response.content
    ```
3. Wie kann man die Überschriften des folgenden HTML-Codes scrapen?
    ```html 
        <!DOCTYPE html>
        <header>
            <title>Hallo Welt!</title>
        </header>
        <html>
            <body>
            <h1 class="headline">1. Lorem Ipsum</h1>
            <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.</p>

            <h1 class="headline">2. Dolor Sit</h1>
            <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.</p>

            <h3 class="headline subheadline">3. Amet</h3>
            <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.</p>
            </body>
        </html>
    ```

    ```python
        soup = BeautifulSoup(html, 'html.parser')
        soup.find_all('h1')
    ```

