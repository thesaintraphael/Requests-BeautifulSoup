# author: Rafael Salimov // https://github.com/thesaintraphael

import requests
from bs4 import BeautifulSoup

rate = float(input('Enter your rating between 8.0 and 9.2: '))  # 8.0 is the minimal rating of movies in top 250.

while rate < 8.0 or rate > 9.2:
    rate = float(input('Please input correctly: ')) 

print("Please wait. Program is taking data. \n")


url = "http://www.imdb.com/chart/top"  # url addres where from we'll get data
response = requests.get(url)    # make program to connect the url address
html_data = response.content    # taking html data of address

soup = BeautifulSoup(html_data, 'html.parser') # using that to take data in more accurate way and parse it
# print(soup.prettify())  # print if you want to see html data

titles = soup.find_all("td", {"class": "titleColumn"})  # all titles' data is shown with "td" tag and "titleColumn class", so we get data ssociated with them. You can check it (right click --> inspect)
ratings = soup.find_all('td', {'class': 'ratingColumn imdbRating'})

for title, rating in zip(titles, ratings):
    title = title.text  # taking only text data from elements
    rating = rating.text

    title = title.strip()       # avoiding extra white spaces
    title = title.replace('\n', '')
    rating = rating.strip()     # avoiding extra white spaces
    rating = rating.replace('\n', '')

    title = title[:3] + title[8:]   # in order to clean title from extra characters /
    # (print title before it to see difference)

    print("Movies: ")
    
    if float(rating) >= rate:   # printing only movies  with rating  that equal and higher than user  input.
        print('{} IMDB rating: {}'.format(title, rating))

