from PIL import Image

link = Image.open('image_link.PNG')
cover = Image.open('cover_image.PNG')
cover = cover.resize(link.size)
cover.putalpha(100)
link.paste(im=cover, box=(0, 0), mask=cover)
link.show()
