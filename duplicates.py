import os
import hashlib

FOLDER_NAME = 'Nika Rome/DCIM/100OLYMP'
for image in os.listdir(FOLDER_NAME):
    with open(FOLDER_NAME + '/' + image,'rb') as fh:
        hasher = hashlib.sha1(fh.read()).hexdigest()
        print image, hasher