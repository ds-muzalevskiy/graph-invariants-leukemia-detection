import numpy as np
import glob,os
import cv2
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

img_path = '../init_cells'
outpath = '../cells'

filenames = glob.glob(img_path + "/**/*.jpg",recursive=True)

for img in filenames:

    if "DS_Store" in img: continue
    src_fname, ext = os.path.splitext(img)

    datagen = ImageDataGenerator(
                             rotation_range=20,
                             brightness_range=[0.15,0.3],
                             zoom_range=[1,0.5])
    img = load_img(img)

    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    img_name = src_fname.split('/')[-1]
    save_fname = outpath

    i = 0
    for batch in datagen.flow (x, batch_size=1, save_to_dir = save_fname,
                               save_prefix = img_name, save_format='jpg'):
        i+=1
        if i>29:
            break
