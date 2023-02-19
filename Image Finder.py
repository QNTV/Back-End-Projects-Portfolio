import re
import requests
from bs4 import BeautifulSoup
import os
import csv

current_directory = os.path.dirname(os.path.abspath(__file__))

with open('sites.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            site = row[0]
            response = requests.get(site)

            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('ignore_js_op')
            print(img_tags)

            urls = [img['zoomfile'] for img in img_tags]

            for url in urls:
                #filename = re.search(r'data/attachment/forum/', url)
                #filename = re.search(r'data/attachment/forum/', url)
                filename = re.search(r'/([\w_-]+[.](jpg|png|jpeg))$', url)
                print(filename)
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
                    if len(response.content) >= 0:
                        f.write(response.content)
