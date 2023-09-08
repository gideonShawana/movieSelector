import requests
from bs4 import BeautifulSoup
import warnings
from urllib3.exceptions import InsecureRequestWarning

url = 'https://www.imdb.com/chart/top'

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('.lister-list tr')

    for movie in movietags:
        title = movie.find('td', class_='titleColumn').a.get_text()
        year = movie.find('span', class_='secondaryInfo').get_text()
        rating = movie.find('td', class_='ratingColumn').strong.get_text()

        print(f'Title: {title}')
        print(f'Year: {year}')
        print(f'Rating: {rating}')
        print()


if __name__ == '__main__':
    main()