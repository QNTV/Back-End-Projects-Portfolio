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
        img_tags = soup.find_all('a')

        urls = [a['href'] for a in img_tags if a.has_attr('href') and '.mp4' in a['href']]

        for url in urls:
            filename = re.search(r'/([\w_-]+[.](mp4))$', url)
            if not filename:
                 print("Regex didn't match with the url: {}".format(url))
                 continue
            with open(os.path.join(current_directory, filename.group(1)), 'wb') as f:
                if 'http' not in url:
                    # sometimes an mp4 source can be relative 
                    # if it is provide the base url which also happens 
                    # to be the site variable atm. 
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                f.write(response.content)
