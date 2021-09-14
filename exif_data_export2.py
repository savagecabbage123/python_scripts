from PIL import Image
from PIL.ExifTags import TAGS
from GPSPhoto import gpsphoto

image = Image.open("img.jpg")
pixels = image.load()
exifdata = {}
out_file = open("img2.bin", "w")
# you need tags to transfer unreadable tag ids into the tag name
for tag, value in image.getexif().items():
    if tag in TAGS:
        exifdata[TAGS[tag]] = value
print(exifdata)
# Get the data from image file and return a dictionary
data = gpsphoto.getGPSData('img.jpg')
print(data['Latitude'], data['Longitude'])
out_file.write(str(exifdata))
out_file.write(str(data))