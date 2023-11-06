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
#         img_tags = soup.find_all('img')
#         print(img_tags)

#         urls = [img['file'] for img in img_tags]

#         for url in urls:
#             #filename = re.search(r'picatt.52av.one/attachments/', url)
#             #filename = re.search(r'https://picatt.52av.one/attachments/*\.jpg$', url)
#             filename = re.search(r'/([\w_-]+[.](jpg|png|jpeg))$', url)
#             print(filename)
#             if not filename:
#                  print("Regex didn't match with the url: {}".format(url))
#                  continue
#             with open(os.path.join(current_directory, filename.group(1)), 'wb') as f:
#                 if 'http' not in url:
#                     # sometimes an image source can be relative
#                     # if it is provide the base url which also happens
#                     # to be the site variable atm.
#                     url = '{}{}'.format(site, url)
#                 response = requests.get(url)
#                 if len(response.content) >= 10000:
#                     f.write(response.content)


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
#         img_tags = soup.find_all('img')
#         print(img_tags)

#         urls = []
#         for img in img_tags:
#             if 'file' in img.attrs:
#                 urls.append(img['file'])
#         print(urls)

#         for url in urls:
#             # filename = re.search(r'picatt.52av.one/attachments/', url)
#             filename=re.search(r'data/attachment/forum/*.jpg', url)
#             # filename = re.search(r'https://picatt.52av.one/attachments/*\.jpg$', url)
#             # filename = re.search(r'/([\w_-]+[.](jpg|png|jpeg))$', url)
#             print(filename)
#             if not filename:
#                  print("Regex didn't match with the url: {}".format(url))
#                  continue
#             with open(os.path.join(current_directory, filename.group(1)), 'wb') as f:
#                 if 'http' not in url:
#                     # sometimes an image source can be relative
#                     # if it is provide the base url which also happens
#                     # to be the site variable atm.
#                     url='{}{}'.format(site, url)
#                 response=requests.get(url)
#                 f.write(response.content)


# Working with 52av.one date:2.18.2023
import re
import requests
from bs4 import BeautifulSoup
import os
import csv

current_directory = r'C:\Users\QuangTrang\source\repos\z'
files = set()

# Read file names from files.csv and add them to the set 'files'
# with open('files.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row:
#             files.add(row[0])
            
with open('sites.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        site = row[0]
        response = requests.get(site)

        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        print(img_tags)

        urls = []
        for img in img_tags:
            if 'file' in img.attrs:
                urls.append(img['file'])
        print(urls, "hello")

        for url in urls:
            # filename = re.search(r'picatt.52av.one/attachments/', url)
            # filename=re.search(r'data/attachment/forum/*.jpg', url)
            # filename = re.search(r'https://picatt.52av.one/attachments/*\.jpg$', url)
            filename = re.search(r'/([\w_-]+[.](jpg|png|jpeg))$', url)
            print(filename)
            url =  url #'https://www.52av.one/' +
            print(url)
            if not filename:
                print("Regex didn't match with the url: {}".format(url))
                continue
            # Check if file already exists before downloading
            if filename.group(1) in files:
                print("File already exists: {}".format(filename.group(1)))

            with open(os.path.join(current_directory, filename.group(1)), 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative
                    # if it is provide the base url which also happens
                    # to be the site variable atm.
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                f.write(response.content)
                # Add filename to the set 'files'
                #files.add(filename.group(1))
                with open('files.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([filename.group(1)])