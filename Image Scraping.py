# import requests
# import csv
# import zipfile
# from bs4 import BeautifulSoup 
# import os

# def download_images(websites, file_name):
#     # Create an empty list to store the image URLs
#     image_urls = []
    
#     # Iterate through the list of websites
#     for website in websites:
        
#         # Use requests to get the HTML data from the website
#         html_data = requests.get(website, verify=False).text     
                
#         # Use BeautifulSoup to parse the HTML data
#         soup = BeautifulSoup(html_data, 'html.parser')
        
#         # Find all the 'img' tags in the HTML data
#         for item in soup.find_all('img'):
#             # Get the 'src' attribute of the 'img' tag
#             image_url = item.get('src')
#             # Check if the 'src' attribute exists
#             if image_url is not None:
#                 # Check if the URL starts with 'http://' or 'https://'
#                 if not image_url.startswith(('http://', 'https://')) and '://' in image_url:
#                     # Add 'http://' to the URL if it does not start with either 'http://' or 'https://'
#                     image_url = 'http://' + image_url
#                 # Add the URL to the list of image URLs
#                 image_urls.append(image_url)
    
#     # Check if the zip file already exists
#     i = 0
#     while os.path.exists(file_name):
#         # Increment the file name if the file already exists
#         i += 1
#         file_name = file_name[:-4] + str(i) + '.zip'
    
#     # Create a zip file with the name ' picture.zip'
#     with zipfile.ZipFile(file_name, 'w') as zip_file:
#         # Iterate through the list of image URLs
#         for url in image_urls:
#             # Use requests to get the image data
#             if url:
#                 if not url.endswith('.gif'):
#                     image_data = requests.get(url).content
#                     # Write the image data to the zip file
#                     zip_file.writestr(url.split("/")[-1], image_data)
#             else:
#                 print("Skipping empty URL.")

# # Read the list of websites from the CSV file
# with open('weblinks.csv', 'r') as csvfile:
#     websites = list(csv.reader(csvfile))

# # Flatten the list of websites
# websites = [item for sublist in websites for item in sublist]

# # Call the function to download the images
# download_images(websites, 'picture.zip')



import requests
import warnings
import csv
import zipfile
from bs4 import BeautifulSoup 
import os
import certifi
import urllib3

def download_images(websites, file_name):
    # Create an empty list to store the image URLs
    image_urls = []
    
    # Iterate through the list of websites
    for website in websites:
        
        # Use requests to get the HTML data from the website
        html_data = requests.get(website, verify=certifi.where()).text
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Use BeautifulSoup to parse the HTML data
        soup = BeautifulSoup(html_data, 'html.parser')
        
        # Find all the 'img' tags in the HTML data
        for item in soup.find_all('img'):
            # Get the 'src' attribute of the 'img' tag
            image_url = item.get('src')
            # Check if the 'src' attribute exists
            if image_url is not None:
                
                if not image_url.startswith(('http://', 'https://')) and '://' in image_url:
                    # Add 'http://' to the URL if it does not start with either 'http://' or 'https://'
                    image_url = 'http://' + image_url

                
                # # Check if the URL starts with 'http://' or 'https://'
                # if not image_url.startswith(('http://', 'https://')) and '://' in image_url:
                #     # Add 'http://' to the URL if it does not start with either 'http://' or 'https://'
                #     image_url = 'http://' + image_url

                # Add the URL to the list of image URLs
                image_urls.append(image_url)
    
    # Check if the zip file already exists
    i = 0
    while os.path.exists(file_name):
        # Increment the file name if the file already exists
        i += 1
        file_name = file_name[:-4] + str(i) + '.zip'
    
    # Create a zip file with the name ' picture.zip'
    with zipfile.ZipFile(file_name, 'w') as zip_file:
        # Iterate through the list of image URLs
        for url in image_urls:
            # Use requests to get the image data
            if url:
                if not url.endswith('.gif'):
                    image_data = requests.get(url).content
                    # Write the image data to the zip file
                    zip_file.writestr(url.split("/")[-1], image_data)
            else:
                print("Skipping empty URL.")

# Read the list of websites from the CSV file
with open('weblinks.csv', 'r') as csvfile:
    websites = list(csv.reader(csvfile))

# Flatten the list of websites
websites = [item for sublist in websites for item in sublist]

# Call the function to download the images
download_images(websites, 'picture.zip')




# import requests
# import warnings
# import csv
# import zipfile
# from bs4 import BeautifulSoup
# import os
# import certifi
# import urllib3
# from selenium import webdriver

# def download_images(websites, file_name):
#     # Create an empty list to store the image URLs
#     image_urls = []
    
#     # Create a webdriver instance
#     driver = webdriver.Firefox()
    
#     # Iterate through the list of websites
#     for website in websites:
#         # Use the webdriver to get the HTML data from the website
#         driver.get(website)
#         html_data = driver.page_source
        
#         # Use BeautifulSoup to parse the HTML data
#         soup = BeautifulSoup(html_data, 'html.parser')
        
#         # Find all the 'img' tags in the HTML data
#         for item in soup.find_all('img'):
#             # Get the 'src' attribute of the 'img' tag
#             image_url = item.get('src')
#             # Check if the 'src' attribute exists
#             if image_url is not None:
                
#                 if not image_url.startswith(('http://', 'https://')) and '://' in image_url:
#                     # Add 'http://' to the URL if it does not start with either 'http://' or 'https://'
#                     image_url = 'http://' + image_url

                
#                 # # Check if the URL starts with 'http://' or 'https://'
#                 # if not image_url.startswith(('http://', 'https://')) and '://' in image_url:
#                 #     # Add 'http://' to the URL if it does not start with either 'http://' or 'https://'
#                 #     image_url = 'http://' + image_url

#                 # Add the URL to the list of image URLs
#                 image_urls.append(image_url)
    
#     # Close the webdriver instance
#     driver.quit()
    
#     # Check if the zip file already exists
#     i = 0
#     while os.path.exists(file_name):
#         # Increment the file name if the file already exists
#         i += 1
#         file_name = file_name[:-4] + str(i) + '.zip'
    
#     # Create a zip file with the name ' picture.zip'
#     with zipfile.ZipFile(file_name, 'w') as zip_file:
#         # Iterate through the list of image URLs
#         for url in image_urls:
#             # Use requests to get the image data
#             if url:
#                 if not url.endswith('.gif'):
#                     image_data = requests.get(url).content
#                     # Write the image data to the zip file
#                     zip_file.writestr(url.split("/")[-1], image_data)
#             else:
#                 print("Skipping empty URL.")

# # Read the list of websites from the CSV file
# with open('weblinks.csv', 'r') as csvfile:
#     websites = list(csv.reader(csvfile))

# # Flatten the list of websites
# websites = [item for sublist in websites for item in sublist]

# # Call the function to download the images
# download_images(websites, 'picture.zip')

