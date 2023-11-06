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


# Working for Rphangx.net
# import re
# import requests
# from bs4 import BeautifulSoup
# import os
# import csv

# current_directory = r'C:\Users\QuangTrang\source\repos\z'

# # Read in the existing urls from the result.csv file
# existing_urls = []
# result_file = os.path.join(current_directory, 'Link Finder.csv')
# if os.path.exists(result_file):
#     with open(result_file, 'r') as file:
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

#         with open(result_file, 'a', newline='') as f:
#             writer = csv.writer(f)
#             for url in urls:
#                 writer.writerow([url])
#                 existing_urls.append(url)



# Working for 52av.one
import re
import requests
from bs4 import BeautifulSoup
import os
import csv

current_directory = r'C:\Users\QuangTrang\source\repos\Back-End-Projects-Portfolio'

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
        print(a_tags,"22222222222222")

        urls = []
        for a in a_tags:
            if 'href' in a.attrs and a['href'].startswith("https://52av.one/thread"):
                url = "" + a['href']
                print(url, "6868686868")
                if url not in existing_urls:
                    urls.append(url)

        with open(result_file, 'a', newline='') as f:
            writer = csv.writer(f)
            for url in urls:
                writer.writerow([url])
                existing_urls.append(url)
                
                
                
# Function that reads in the Link Finder.csv file, removes duplicate URLs, and writes the results to a new file remove_duplicate_link_finder.csv:                
import csv

def remove_duplicates():
    current_directory = r'C:\Users\QuangTrang\source\repos\Back-End-Projects-Portfolio\Link Finder.csv'
    with open(current_directory, 'r') as infile:
        reader = csv.reader(infile)
        urls = []
        for row in reader:
            url = row[0]
            if url not in urls:
                urls.append(url)

    with open('remove_duplicate_link_finder.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for url in urls:
            writer.writerow([url])

remove_duplicates()