from imgAugBoundingBox import *
import cv2
import os

CATEGORIES = ["AyamBrand_Sardines_425g", "AyamBrand_Sardines_Flat", "Camel Baked Almond", "Camel Baked Pistachio", "FarmHouse Fresh Milk Pasteurised", "FarmHouse Fresh Milk UHT",
              "Marigold HL Milk Large", "Marigold HL Milk LBC"]

# imageInput = cv2.imread('datasets/images/AyamBrand_Sardines_425g/AYAMBRAND_SARDINES_425G0001.jpg')
DATADIR = 'dataset'

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        for img in os.listdir(path):
            try:
                infile = os.path.join(path, img)
                print(infile)
                dataAug(infile)
            except Exception as e:
                pass


create_training_data()