from PIL import Image, ImageEnhance, ImageFilter
import os 

path = './images'
pathout = '/editedImages'

for filename in os.listdir(path):
    image = Image.open(f"{path}/{pathout}")\
    
    edit = image.filter(ImageFilter.SHARPEN)#.convert('L").rotate(-90)#
    
    #for enhancing contrast
    
    '''factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)'''
    
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f'.{pathout}/{clean_name}_edit.jpg')