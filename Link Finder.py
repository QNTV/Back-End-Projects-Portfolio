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



# Remove duplicate from the result.

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

                #         urls = []
                #         for a in a_tags:
                #             if 'href' in a.attrs and a['href'].startswith("/threads/"):
                #                 urls.append("https://rphangx.net" + a['href'])

                #         # Remove duplicates from the list of URLs
                #         urls = list(set(urls))

                #         with open('result.csv', 'a', newline='') as f:
                #             writer = csv.writer(f)
                #             for url in urls:
                #                 writer.writerow([url])


# # Remove duplicate from the existing result.
# import re
# import requests
# from bs4 import BeautifulSoup
# import os
# import csv



# #current_directory = os.path.dirname(os.path.abspath(__file__))

# # Read in the existing urls from the result.csv file
# existing_urls = []
# result_file = os.path.join(current_directory, 'result.csv')
# if os.path.exists('result.csv'):
#     with open('result.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             existing_urls.append(row[0])

# # Append new urls to the existing urls list
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
#                 url = "https://rphangx.net" + a['href']
#                 if url not in existing_urls:
#                     urls.append(url)

#         with open('result.csv', 'a', newline='') as f:
#             writer = csv.writer(f)
#             for url in urls:
#                 writer.writerow([url])
#                 existing_urls.append(url)



import re
import requests
from bs4 import BeautifulSoup
import os
import csv

current_directory = r'C:\Users\QuangTrang\source\repos\z'

# Read in the existing urls from the result.csv file
existing_urls = []
result_file = os.path.join(current_directory, 'Link Finder.csv')
if os.path.exists(result_file):
    with open(result_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            existing_urls.append(row[0])

# Append new urls to the existing urls list
with open('sites.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        site = row[0]
        response = requests.get(site)

        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a')
        print(a_tags)

        urls = []
        for a in a_tags:
            if 'href' in a.attrs and a['href'].startswith("/threads/"):
                url = "https://rphangx.net" + a['href']
                if url not in existing_urls:
                    urls.append(url)

        with open(result_file, 'a', newline='') as f:
            writer = csv.writer(f)
            for url in urls:
                writer.writerow([url])
                existing_urls.append(url)
