import requests
from bs4 import BeautifulSoup

rate = float(input('Enter your rating between 8.0 and 9.2: '))

while rate < 8.0 or rate > 9.2:
    rate = float(input('Please input correctly: '))



url = "http://www.imdb.com/chart/top"
response = requests.get(url)
html_data = response.content

soup = BeautifulSoup(html_data, 'html.parser')

titles = soup.find_all("td", {"class": "titleColumn"})
ratings = soup.find_all('td', {'class': 'ratingColumn imdbRating'})

for title, rating in zip(titles, ratings):
    title = title.text
    rating = rating.text

    title = title.strip()       # avoiding extra white spaces
    title = title.replace('\n', '')
    rating = rating.strip()     # avoiding extra white spaces
    rating = rating.replace('\n', '')

    title = title[:3] + title[8:]   # in order to clean title from extra characters /
    # (print title before it to see difference)

    if float(rating) >= rate:
        print('Movie: {} IMDB rating: {}'.format(title, rating))

