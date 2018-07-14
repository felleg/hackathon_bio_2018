import pandas as pd
import numpy as np
import cv2
import tensorflow as tf

truth = pd.read_csv('ISIC2018_Task3_Training_GroundTruth/ISIC2018_Task3_Training_GroundTruth.csv')

# Sample 1% of the data for development because my computer is bad
truth = truth.sample(frac=0.01)

rgb = []

# Loop over melanomas
for index in range(len(truth)):
    if index%100 == 0:
        print(str(index) + ' / ' + str(len(truth)))
    image = truth.iloc[index].image
    rgb += [cv2.imread('ISIC2018_Task3_Training_Input/'+image+'.jpg')]

# RGB information stored in truth array
truth['rgb'] = rgb
