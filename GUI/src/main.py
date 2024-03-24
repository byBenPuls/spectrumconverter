import customtkinter
# import tkinter as tk
from tkinter import filedialog
from PIL import Image
import webbrowser
# from tkinter import messagebox

# import temp.actions.load as load

filepath = None


def button_callback():
    filename = filedialog.askopenfilename(
        filetypes=[('XML спектр', '*.xml'), ('CSV спектр', '*.csv')],
        title='Выберите спектр в формате .xml или .csv'
    )
    if filename:
        # load.SaveNewPath(filename)
        path_to_file = filename
        button.configure(text=path_to_file.split('/')[-1])
        button1.configure(state=customtkinter.NORMAL)
        # tk.messagebox.showerror('Произошла ошибка!', 'Попробуйте использовать другой файл')
    else:
        print('No file selected')


def converting():
    print('Converting')


def github_link():
    webbrowser.open('https://github.com/byBenPuls/spectrumconverter')


app = customtkinter.CTk()
app.geometry('450x250')
app.title('Spectrum Converter')
app.iconbitmap('../resources/icons/icon.ico')
app.resizable(False, False)
app.grid_columnconfigure((0), weight=1)
app.grid_rowconfigure((0), weight=1)
button = customtkinter.CTkButton(app, text='Нажмите, чтобы выбрать файл', command=button_callback)
button.grid(column=0, row=0)
button1 = customtkinter.CTkButton(app, text='конвертировать',
                                  border_width=1,
                                  state=customtkinter.DISABLED,
                                  fg_color='green',
                                  hover_color='#005B00',
                                  command=converting,
                                  height=40)
button1.grid(column=0, row=1)

github_image = customtkinter.CTkImage(Image.open('../resources/icons/github-mark-white.png'),
                                      size=(30, 30))

image_label = customtkinter.CTkButton(app, image=github_image, text='',
                                      fg_color='transparent', hover=False,
                                      command=github_link,
                                      width=30)
image_label.grid(column=3, row=3)

app.mainloop()
