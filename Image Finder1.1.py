# from bs4 import BeautifulSoup
# from urllib2 import urlopen
# import urllib

# # use this image scraper from the location that 
# #you want to save scraped images to
# url = https://www.52av.one/thread-126189-1-1.html
# def make_soup(url):
#     html = urlopen(url).read()
#     return BeautifulSoup(html)

# def get_images(url):
#     soup = make_soup(url)
#     #this makes a list of bs4 element tags
#     images = [img for img in soup.findAll('img')]
#     print (str(len(images)) + "images found.")
#     print 'Downloading images to current working directory.'
#     #compile our unicode list of image links
#     image_links = [each.get('src') for each in images]
#     for each in image_links:
#         filename=each.split('/')[-1]
#         urllib.urlretrieve(each, filename)
#     return image_links

# #a standard call looks like this
# #get_images('http://www.wookmark.com')


# from bs4 import BeautifulSoup
# import urllib.request

# def make_soup(url):
#     html = urllib.request.urlopen(url).read()
#     return BeautifulSoup(html, "html.parser")

# def get_images(url):
#     soup = make_soup(url)
#     # this makes a list of bs4 element tags
#     images = [img for img in soup.findAll('img')]
#     print(str(len(images)) + " images found.")
#     print('Downloading images to the current working directory.')
#     # compile our unicode list of image links
#     image_links = [each.get('src') for each in images]
#     for each in image_links:
#         filename = each.split('/')[-1]
#         urllib.request.urlretrieve(each, filename)
#     return image_links

# # use this image scraper from the location that 
# # you want to save scraped images to
# url = "https://www.52av.one/thread-126189-1-1.html"
# get_images(url)

from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
from urllib.parse import urljoin
import sys
import time

def make_soup(url):
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    html = urllib.request.urlopen(req)
    return BeautifulSoup(html, 'html.parser')

def get_images(url):
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + " images found.")
    print('Downloading images to current working directory.')
    image_links = [each.get('src') for each in images]
    for each in image_links:
        try:
            filename = each.strip().split('/')[-1].strip()
            src = urljoin(url, each)
            print('Getting: ' + filename)
            response = requests.get(src, stream=True)
            # delay to avoid corrupted previews
            time.sleep(1)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except:
            print('  An error occured. Continuing.')
    print('Done.')

if __name__ == '__main__':
    get_images('https://rphangx.net/threads/lan-dau-khoe-lol-vk.150641/')