

# for python scrapping

|   Method   |  parameter  |                |
|---------------|-----------------|----------------|
|    requests.get | request_file = requests.get(self.url)| url[string]|
|BeautifulSoup|BeautifulSoup(request_file.text, 'html.parser') |request_file[html] |
|BeautifulSoup.select('a[class=link-container__link]')| a | a[string] |
|BeautifulSoup.find('div', {'class': 'heading-with-meta'}).findChild('h5')| a, b| a[str], b[dict]|
|BeautifulSoup.find_all('td', {'class':'column-width--70pc'})|a, b|a[str], b[dict]|


