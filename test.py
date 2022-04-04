# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pdf2image import convert_from_path
import cv2
import pytesseract
from collections import defaultdict

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
config = ('-l kor+eng --oem 3')
file_name = 'JLL_Leasing Flyer_2020_June_Final_compressed.pdf'
pages = convert_from_path('data/'+file_name)

for i, page in enumerate(pages):
    print(len(pages))

img = pages[11]

building_image_position = (0,0,700,1200)
building_image = img.crop(building_image_position)
building_image.show()

location_position = (700,0,1400,600)
location_image = img.crop(location_position)
location_image.show()

floor_plan_position = (1500,0,2000,500)
floor_plan_image = img.crop(floor_plan_position)
floor_plan_image.show()

general_info_area = (700,600,1500,1300)
general_info_image = img.crop(general_info_area)
general_info_image.show()

space_availability_position = (1500,600,2600,1300)
space_availability_image = img.crop(space_availability_position)
space_availability_image.show()

building_image.save('8'+'_'+'building.jpg')
location_image.save('8'+'_'+'location.jpg')
floor_plan_image.save('8'+'_'+'floor_plan.jpg')
general_info_image.save('8'+'_'+'general_info.jpg')
space_availability_image.save('8'+'_'+'space_availability.jpg')


general_info = pytesseract.image_to_string(general_info_image, config=config)
general_info = general_info.replace('ABZ (GFA)', '연면적 (GFA)')
general_info = general_info.split('\n')
general_info = [v for v in general_info if v]

general_columns = ['General Information','주소','준공연도','연면적 (GFA)','빌딩규모','기준층면적','전용률','엘리베이터','천정고','위치']

general_info_dict = defaultdict(list)

for i, info in enumerate(general_info):
    for j in general_columns:
        if(j in info):
            col = info[0:len(j)]
    print(i)    
    print(col)
    print(info)
    general_info_dict[col].append(info.strip(col).strip())

print(general_info_dict)


space_availability = pytesseract.image_to_string(space_availability_image, config=config)
space_availability = space_availability.replace('VATH.E', 'VAT별도')
space_availability = space_availability.split('\n')
space_availability = [v for v in space_availability if v]
