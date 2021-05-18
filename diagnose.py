#!/usr/bin/python

import os
import time

import nibabel as nib
import numpy as np
from nilearn.image import resample_img

from tensorflow import keras

start_time = time.time()

filename = 'uploaded_file.nii'
uploaded_file = os.path.join('/var','www','html','uploads', filename)

# Image Resize
# C1
X1 = np.empty((1,256,256,3,1))
image = nib.load(os.path.join('/var','www','html','uploads', 'c1' + filename))
my_image = resample_img(image, target_affine=np.eye(4), target_shape=(256,256,166))
data = my_image.get_fdata()
data = np.expand_dims(data, axis=3) 
midpoint = round(np.size(data,2)/2)
data = data[:, :, midpoint-2:midpoint+1]
X1[0,] = data

# C2
X2 = np.empty((1,256,256,3,1))
image = nib.load(os.path.join('/var','www','html','uploads', 'c2' + filename))
my_image = resample_img(image, target_affine=np.eye(4), target_shape=(256,256,166))
data = my_image.get_fdata()
data = np.expand_dims(data, axis=3) 
midpoint = round(np.size(data,2)/2)
data = data[:, :, midpoint-2:midpoint+1]
X2[0,] = data

# C3
X3 = np.empty((1,256,256,3,1))
image = nib.load(os.path.join('/var','www','html','uploads', 'c3' + filename))
my_image = resample_img(image, target_affine=np.eye(4), target_shape=(256,256,160))
data = my_image.get_fdata()
data = np.expand_dims(data, axis=3) 
midpoint = round(np.size(data,2)/2)
data = data[:, :, midpoint-2:midpoint+1]
X3[0,] = data

# Load Neural Networks
model1 = keras.models.load_model('/var/www/html/NN_models/my_model_load_three_c1/')
model2 = keras.models.load_model('/var/www/html/NN_models/my_model_load_three_c2/')
model3 = keras.models.load_model('/var/www/html/NN_models/my_model_load_three_c3/')

# Predict
prediction1 = model1.predict(X1)[0]
prediction2 = model2.predict(X2)[0]
prediction3 = model3.predict(X3)[0]

ADconfidence = (prediction1[0]+prediction2[0]+prediction3[0])/3
MCIconfidence = (prediction1[1]+prediction2[1]+prediction3[1])/3
CNconfidence = (prediction1[2]+prediction2[2]+prediction3[2])/3

if (ADconfidence > MCIconfidence) and (ADconfidence > CNconfidence):
    classification = "AD"
    confidence = ADconfidence
elif (MCIconfidence > ADconfidence) and (MCIconfidence > CNconfidence):
    classification = "MCI"
    confidence = MCIconfidence
elif (CNconfidence > ADconfidence) and (CNconfidence > MCIconfidence):
    classification = "CN"
    confidence = CNconfidence

print("Class: ", classification, "   Confidence score: ", round(confidence*100,2),"%")
