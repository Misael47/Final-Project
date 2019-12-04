from PIL import Image, ImageDraw, ImageFont

image = Image.open('Taco photo.jpg')
# opens downloaded image from Unsplash
width = image.width
height = image.height
print(width, height)
#This checks the origanal images aspect ratio
Smaller_image = image.resize((333, 333))
# This reduces the image to less than 800px
font = ImageFont.truetype('DejaVuSans.ttf', 27)
# font size and format
img_draw= ImageDraw.Draw(image)
img_draw.text([50, 200], 'Random Taco Cookbook', fill='Green', font=font)
# Will place text in desired coordinates with the color of your choice
image.save('Modified_TacoPhoto.jpg')
# saves image, can save under new name or replace old image