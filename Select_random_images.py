#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil
import random

# Define the name of the main folder
main_folder = '/home/ihs/udentify/f1_p1'

# Define the name of the target folder
target_folder = '/home/ihs/udentify/processed'

# Iterate through all folders in the main folder
for folder_name in os.listdir(main_folder):
    # Create folder path
    folder_path = os.path.join(main_folder, folder_name)
    
    # Skip if it's not a folder (i.e., it's a file)
    if not os.path.isdir(folder_path):
        continue
    
    # Create a folder with the same name in the target folder
    target_folder_path = os.path.join(target_folder, folder_name)
    os.makedirs(target_folder_path, exist_ok=True)
    
    # Get all images in the folder
    images = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    
    # Select up to 10 random images
    selected_images = random.sample(images, min(len(images), 10))
    
    # Copy the selected images to the target folder and rename them
    for idx, image in enumerate(selected_images, start=1):
        image_path = os.path.join(folder_path, image)
        target_image_path = os.path.join(target_folder_path, f"{folder_name}_{idx}.jpg")
        shutil.copy(image_path, target_image_path)

