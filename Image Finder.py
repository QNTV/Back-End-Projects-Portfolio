import re
import requests
from bs4 import BeautifulSoup
import os
import csv

current_directory = os.path.dirname(os.path.abspath(__file__))

with open('sites.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        site = row[0]
        response = requests.get(site)

        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        urls = [img['src'] for img in img_tags]

        for url in urls:
            filename = re.search(r'/([\w_-]+[.](jpg|png|jpeg))$', url)
            if not filename:
                 print("Regex didn't match with the url: {}".format(url))
                 continue
            with open(os.path.join(current_directory, filename.group(1)), 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative 
                    # if it is provide the base url which also happens 
                    # to be the site variable atm. 
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                if len(response.content) >= 100000:
                    f.write(response.content)
