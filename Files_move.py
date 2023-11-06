# import shutil
# import os

# # Define the source and destination folders
# source_folder = r"C:\Users\QuangTrang\Desktop\baby camera\record\20230719\23"
# destination_folder = r"C:\Users\QuangTrang\Desktop\baby camera\record\20230719"

# # Get the list of all files in the source folder
# files = os.listdir(source_folder)

# # Iterate over the list of files and move them to the destination folder
# for file in files:
#     shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))

# # Print a message to the console
# print("All files have been moved from {} to {}.".format(source_folder, destination_folder))


# import os
# import shutil

# # Define the source and destination folders
# source_folder = r"C:\Users\QuangTrang\Desktop\baby camera\record\20230719"
# destination_folder = r"C:\Users\QuangTrang\Desktop\baby camera\record\20230719\test"

# # Get a list of all subfolders in the source folder
# subfolders = os.listdir(source_folder)

# # Iterate over the list of subfolders
# for subfolder in subfolders:

#     # Get the path to the subfolder
#     subfolder_path = os.path.join(source_folder, subfolder)

#     # Get the list of all files in the subfolder
#     files = os.listdir(subfolder_path)

#     # Iterate over the list of files and move them to the destination folder
#     for file in files:
#         shutil.move(os.path.join(subfolder_path, file), os.path.join(destination_folder, file))

# # Print a message to the console
# print("All files have been moved from {} to {}.".format(source_folder, destination_folder))



import os
import shutil

source_folder = r"C:\Users\QuangTrang\Desktop\baby camera\record\20230818"
destination_folder = r"C:\Users\QuangTrang\Desktop\baby camera\record\20230818"

subfolders = os.listdir(source_folder)

for subfolder in subfolders:

    subfolder_path = os.path.join(source_folder, subfolder)

    files = os.listdir(subfolder_path)

    for file in files:
        # Add the subfolder's name as a prefix to the file name
        new_file_name = f"{subfolder}_{file}"

        # Move the file to the destination folder with the new file name
        shutil.move(os.path.join(subfolder_path, file), os.path.join(destination_folder, new_file_name))

print("All files have been moved from {} to {} with prefix.".format(source_folder, destination_folder))
