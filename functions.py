from tkinter import *
from PIL import Image, ImageTk

def display_logo(url, row, column):
    #Logo
    logo = Image.open(url)
    logo = logo.resize((int(logo.size[0]/1.5), int(logo.size[1]/1.5)))
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(image = logo, bg="white")
    logo_label.image = logo
    logo_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)

def display_icon(url, row, column, stick):
    #Logo
    icon = Image.open(url)
    icon = icon.resize((20,20))
    icon = ImageTk.PhotoImage(icon)
    icon_label = Button(image = icon, width=25, height=25)
    icon_label.image = icon
    icon_label.grid(column=column, row=row, sticky=stick)

def display_textbox(content, ro, col, root):
    #TextBox
    text_box = Text(root, height=10 , width=30, padx=10, pady=10)
    text_box.insert(1.0, content)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=col, row=ro, sticky=SW, padx=25, pady=25)

def extract_images(page):
        images = []
        if '/XObject' in page['/Resources']:
            xObject = page['/Resources']['/XObject'].getObject()

            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                    data = xObject[obj].getData()
                    mode = ""
                    if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                        mode = "RGB"
                    else:
                        mode = "CMYK"
                    img = Image.frombytes(mode, size, data)
                    images.append(img)
        return images

def resize_image(img):
    width, height = int(img.size[0]), int(img.size[1])
    if width > height:
        height = int(300/width*height)
        width = 300
    elif height > width:
        width = int(250/height*width)
        height = 250
    else:
        width, height = 250,250
    img = img.resize((width, height))
    return img


def display_images(img):
    img = resize_image(img)
    img = ImageTk.PhotoImage(img)
    img_label = Label(image = img, bg="white")
    img_label.image = img
    img_label.grid(row=4, column=2, rowspan=2)
    return img_label
