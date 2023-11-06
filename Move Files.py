import shutil
import os

def move_files_from_subfolders(source_root, destination_root):
    try:
        # Ensure the destination directory exists
        if not os.path.exists(destination_root):
            os.makedirs(destination_root)

        # Iterate through all items in the source directory
        for item in os.listdir(source_root):
            full_item_path = os.path.join(source_root, item)
            
            # If the item is a directory, move its contents to a new location
            if os.path.isdir(full_item_path):
                # Create a corresponding directory in the destination root
                destination_path = os.path.join(destination_root, item)
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                
                # Get all files in the sub-directory
                sub_items = os.listdir(full_item_path)
                for sub_item in sub_items:
                    full_sub_item_path = os.path.join(full_item_path, sub_item)
                    if os.path.isfile(full_sub_item_path):
                        # Move each file to the new destination
                        shutil.move(full_sub_item_path, destination_path)

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
source_root = "C:\Users\QuangTrang\Desktop\baby camera\record\20230713\19"  # replace with your source folder path
destination_root = "C:\Users\QuangTrang\Desktop\baby camera\record\20230713\20"  # replace with your destination folder path

move_files_from_subfolders(source_root, destination_root)
