from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import (display_logo,
                      display_textbox,
                      extract_images,
                      display_icon,
                      resize_image,
                      display_images)

page_cotents = []
all_images = []

def copy_text(content):
    root.clipboard_clear()
    root.clipboard_append(content[-1])

root = Tk()

root.geometry('+%d+%d'%(1250,10))

#header area
header = Frame(root, width=800, height=175, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

#main_content area
canvas = Frame(root, width=800, height=250, bg="#20bebe")
canvas.grid(columnspan=3, rowspan=2, row=4)

#Instructions
Instructions = Label(root, text="Select a PDF file", font=("Raleway", 10), bg="white")
Instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)

def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("PDF file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        page_content = page_content.replace('\u2122', "'")
        page_cotents.append(page_content)


        images = extract_images(page)

        for i in images:
            all_images.append(i)
            
        img = images[0]

        display_images(img)

        display_textbox(page_content, 4, 0, root)

        browse_text.set("Browse")

        img_menu = Frame(root, width=800, height=60, bg="#c8c8c8")
        img_menu.grid(columnspan=3, rowspan=1, row=2)

        what_img = Label(root, text="image 1 of 5", font=("shanti", 10))
        what_img.grid(row=2, column=1)

        display_icon('arrow_l.png', 2, 0, E)
        display_icon('arrow_r.png', 2, 2, W)

        save_img = Frame(root, width=800, height=60, bg="#c8c8c8")
        save_img.grid(columnspan=3, rowspan=1, row=3)

        copyText_btn = Button(root, text="Copy text", command=lambda:copy_text(page_cotents), font=("shanti", 10), height=1, width=15)
        saveAll_btn = Button(root, text="Save all images", font=("shanti", 10), height=1, width=15)
        save_btn = Button(root, text="Save image", font=("shanti", 10), height=1, width=15)

        copyText_btn.grid(row=3, column=0)
        saveAll_btn.grid(row=3, column=1)
        save_btn.grid(row=3, column=2)

display_logo('logo.png', 0, 0)

#Browse button
browse_text = StringVar()
browse_btn = Button(root,
                    textvariable=browse_text,
                    command=lambda:open_file(),
                    font="Raleway",
                    bg="#20bebe",
                    fg="white",
                    height=2,
                    width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)

root.mainloop()
