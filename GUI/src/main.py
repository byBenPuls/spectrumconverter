import customtkinter
# import tkinter as tk
from tkinter import filedialog

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


app = customtkinter.CTk()
app.geometry('450x250')
app.title('Spectrum Converter')
app.iconbitmap('../resources/icons/icon.ico')
app.resizable(False, False)

button = customtkinter.CTkButton(app, text='Нажмите, чтобы выбрать файл', command=button_callback)
button.pack(padx=20, pady=20)
button1 = customtkinter.CTkButton(app, text='конвертировать',
                                  border_width=1,
                                  state=customtkinter.DISABLED,
                                  fg_color='green',
                                  hover_color='#005B00',
                                  command=converting)
button1.pack(padx=20, pady=70)

app.mainloop()
