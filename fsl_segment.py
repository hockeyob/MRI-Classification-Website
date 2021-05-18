#!/usr/bin/python

import cgitb
import os
import time

import nibabel as nib
import nipype.interfaces.spm as spm

start_time = time.time()

cgitb.enable()

os.environ['SPM_PATH'] = '/var/www/html/spm12/spm12'
spm.SPMCommand.set_mlab_paths(paths=os.environ['SPM_PATH'], matlab_cmd='/usr/local/matlab/R2021a/bin/matlab') 

if "ADexample.nii" in os.listdir(os.path.join('/var','www','html','uploads')):
    filename = "ADexample.nii"

elif "MCIexample.nii" in os.listdir(os.path.join('/var','www','html','uploads')):
    filename = "MCIexample.nii"

elif "CNexample.nii" in os.listdir(os.path.join('/var','www','html','uploads')):
    filename = "CNexample.nii"

else:
    filename = 'uploaded_file.nii'

uploaded_file = os.path.join('/var','www','html','uploads', filename)

# Image Segmentation
seg = spm.NewSegment()
seg.inputs.channel_files = uploaded_file
seg.run()

print ("My program took", time.time() - start_time, "to run")

