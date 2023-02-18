import os
import csv

folder_directory = r'C:\Users\qnguyen\Downloads\Back-End-Projects-Portfolio'
output_file = 'files.csv'

# Get a list of all the files in the directory
file_names = os.listdir(folder_directory)

# Write the list of file names to a CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for file_name in file_names:
        writer.writerow([file_name])
