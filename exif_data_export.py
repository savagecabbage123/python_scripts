from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open("img.jpg")
pixels = image.load()
exifdata = image.getexif()
out_file = open("img.bin", "w")
# you need tags to transfer unreadable tag ids into the tag name
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes of info
    if isinstance(data, bytes):
        data = data.decode()
    out_file.write(f"{tag}: {data}\n")
