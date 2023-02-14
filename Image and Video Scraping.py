# import re
# import requests
# from bs4 import BeautifulSoup
# import os
# import csv

# current_directory = os.path.dirname(os.path.abspath(__file__))

# with open('sites.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if row:
#             site = row[0]
#             response = requests.get(site)

#             soup = BeautifulSoup(response.text, 'html.parser')
#             a_tags = soup.find_all('a')

#             urls = [a['href'] for a in a_tags if a.has_attr('href') and ('.mp4' in a['href'] or '.jpg' in a['href'] or '.png' in a['href'] or '.jpeg' in a['href'])]

#             for url in urls:
#                 filename = re.search(r'/([\w_-]+[.](mp4|jpg|png|jpeg))$', url)
#                 print(filename)
#                 if not filename:
#                     print("Regex didn't match with the url: {}".format(url))
#                     continue
#                 with open(os.path.join(current_directory, filename.group(1)), 'wb') as f:
#                     if 'http' not in url:
#                         # sometimes an image/video source can be relative 
#                         # if it is provide the base url which also happens 
#                         # to be the site variable atm. 
#                         url = '{}{}'.format(site, url)
#                     response = requests.get(url)
#                     f.write(response.content)

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
            a_tags = soup.find_all('a')
            img_tags = soup.find_all('img')

            urls = [a['href'] for a in a_tags if a.has_attr('href') and '.mp4' in a['href']]

            for url in urls:
                filename = re.search(r'/([\w_-]+[.]mp4)$', url)
                print(filename)
                if not filename:
                    print("Regex didn't match with the url: {}".format(url))
                    continue
                with open(os.path.join(current_directory, filename.group(1)), 'wb') as f:
                    if 'http' not in url:
                        # sometimes an image/video source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        url = '{}{}'.format(site, url)
                    response = requests.get(url)
                    f.write(response.content)

            img_urls = [img['src'] for img in img_tags if img.has_attr('src') and ('.jpg' in img['src'] or '.png' in img['src'] or '.jpeg' in img['src'])]

            for img_url in img_urls:
                filename = re.search(r'/([\w_-]+[.](jpg|png|jpeg))$', img_url)
                print(filename)
                if not filename:
                    print("Regex didn't match with the url: {}".format(img_url))
                    continue
                with open(os.path.join(current_directory, filename.group(1)), 'wb') as f:
                    if 'http' not in img_url:
                        # sometimes an image/video source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        img_url = '{}{}'.format(site, img_url)
                    response = requests.get(img_url)
                    f.write(response.content)
