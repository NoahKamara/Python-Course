from bs4 import BeautifulSoup
html = """
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

            <h1 class="headline subheadline">3. Amet</h3>
            <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.</p>
            </body>
        </html>
        """

soup = BeautifulSoup(html, 'html.parser')
soup.find_all('h1')
