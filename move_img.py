# Use this script to move the images in a folder matching their category

import os
import pandas as pd

truth = pd.read_csv('ISIC2018_Task3_Training_GroundTruth/ISIC2018_Task3_Training_GroundTruth.csv')
categories = ["MEL",
            "NV",
            "BCC",
            "AKIEC",
            "BKL",
            "DF",
            "VASC"]


# Move images to their belonging directory
for index, row in truth.iterrows():
    for c in categories:
        # Create category folders (if they do not already exist)
        if not os.path.exists(c):
            os.mkdir(c)
            print("Created folder ", c)
        if row[c] == 1: # The image is in the category with number 1 in its column
            original_directory = 'ISIC2018_Task3_Training_Input/'
            image = row.image+'.jpg'
            destination = c+'/'+image
            # The image file is moved by this command
            try:
                os.rename(original_directory+image, destination)
                print("moved %s to %s"%(image, destination))
            except Exception as e:
                print(e)

