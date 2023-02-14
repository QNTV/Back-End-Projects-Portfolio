# Working but it will return the duplicte
                # import re
                # import requests
                # from bs4 import BeautifulSoup
                # import os
                # import csv

                # current_directory = os.path.dirname(os.path.abspath(__file__))

                # with open('sites.csv', 'r') as file:
                #     reader = csv.reader(file)
                #     for row in reader:
                #         site = row[0]
                #         response = requests.get(site)

                #         soup = BeautifulSoup(response.text, 'html.parser')
                #         a_tags = soup.find_all('a')
                #         print(a_tags)

                #         urls = []
                #         for a in a_tags:
                #             if 'href' in a.attrs and a['href'].startswith("/threads/"):
                #                 urls.append("https://rphangx.net" + a['href'])

                #         with open('result.csv', 'a', newline='') as f:
                #             writer = csv.writer(f)
                #             for url in urls:
                #                 writer.writerow([url])



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
        a_tags = soup.find_all('a')

        urls = []
        for a in a_tags:
            if 'href' in a.attrs and a['href'].startswith("/threads/"):
                urls.append("https://rphangx.net" + a['href'])

        # Remove duplicates from the list of URLs
        urls = list(set(urls))

        with open('result.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            for url in urls:
                writer.writerow([url])
