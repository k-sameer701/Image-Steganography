from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
from stegano import lsb

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()

root.geometry('800x700')
root.title('Image Steganography')
root.maxsize(950, 700)

tabview = customtkinter.CTkTabview(master=root, height=600, width=680)
tabview.pack(padx=20, pady=20)

tabview.add("Hide Data")    
tabview.add("Show Data")    
tabview.set("Hide Data") 

#=========================== HIDE IMAGE ========================================================

def hide_image():
    global images_location, x
    filename_location = (filedialog.askopenfilename(title='Select A File'))
    x=filename_location
    images_location = filename_location
    hide_resize(filename_location)

def hide_resize(event):
    img = (Image.open(event))
    resized_image = img.resize((800, 600), Image.LANCZOS)
    hide_open_image(resized_image)

def hide_open_image(event):
    global images_location, image_select
    image_select = ImageTk.PhotoImage(event)
    image_location = Label(text=images_location)
    image_open = Label(master=tabview.tab("Hide Data"), image=image_select).pack()



hide_button = customtkinter.CTkButton(master=tabview.tab("Hide Data"), text='Select Image', command=hide_image)
hide_button.pack(pady=10)

#======================== SHOW IMAGE ========================================================

def show_image():
    global images_location, y
    filename_location = (filedialog.askopenfilename(title='Select A File'))
    y=filename_location
    images_location = filename_location
    show_resize(filename_location)

def show_resize(event):
    img = (Image.open(event))
    resized_image = img.resize((800, 600), Image.LANCZOS)
    show_open_image(resized_image)

def show_open_image(event):
    global images_location, image_select
    image_select = ImageTk.PhotoImage(event)
    image_open = Label(master=tabview.tab("Show Data"), image=image_select).pack()

show_button = customtkinter.CTkButton(master=tabview.tab("Show Data"), text='Select Image', command=show_image)
show_button.pack(pady=10)

#============================ LOGIC ================================================================

def hide_lsb():
    message_hide = text1.get(1.0, END)
    secret = lsb.hide(str(x), message_hide)
    secret.save('Untitled.png')

def show_lsb():
    text_hidden = lsb.reveal(y)
    clear_message = "Encrypted Message: " + text_hidden
    response = messagebox.showinfo('Show Data', clear_message)


#========================= ENCRYPT BUTTON ========================================================

button_encrypt = customtkinter.CTkButton(master=tabview.tab("Hide Data"), text="Encrypt", command=hide_lsb)
button_encrypt.pack(side=BOTTOM, pady=3)

text1 = customtkinter.CTkTextbox(master=tabview.tab("Hide Data"), width=500, height=2)
text1.pack(side=BOTTOM, pady=5)

#========================= DECRYPT BUTTON ============================================================


button_decrypt = customtkinter.CTkButton(master=tabview.tab("Show Data"), text="Decrypt", command=show_lsb)
button_decrypt.pack(side=BOTTOM, pady=3)

#=============================== END =============================================================

root.mainloop()