import requests
from bs4 import BeautifulSoup
import csv

def refined(s):
    #1,845 total ratings
    r = s.split(' ')[0]
    # res = r.replace(',', '')
    return r.replace(',', '')

def write_csv(data):
    with open('parse.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']
                         ))

def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h3').text
        link = plugin.find('h3').find('a').get('href')
        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(r)
        # print(rating)

        data = {'name': name,
                'url': link,
                'reviews': rating
                }
        # print(data)
        write_csv(data)
    # return len(plugins)


def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()