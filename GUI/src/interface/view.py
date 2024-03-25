import customtkinter
from customtkinter import NORMAL
from tkinter.filedialog import askopenfilename
from PIL import Image
import webbrowser


class MainWindow(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        w = 450
        h = 250

        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.title('Spectrum Converter')
        self.iconbitmap('../resources/icons/icon.ico')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.button = customtkinter.CTkButton(self, text='Нажмите, чтобы выбрать файл', command=self.button_callback)
        self.button.grid(column=0, row=0)
        self.button1 = customtkinter.CTkButton(self, text='конвертировать',
                                               border_width=1,
                                               state=customtkinter.DISABLED,
                                               fg_color='green',
                                               hover_color='#005B00',
                                               command=self.converting,
                                               height=40)
        self.button1.grid(column=0, row=1)

        self.github_image = customtkinter.CTkImage(Image.open('../resources/icons/github-mark-white.png'),
                                                   size=(30, 30))

        self.image_label = customtkinter.CTkButton(self, image=self.github_image, text='',
                                                   fg_color='transparent', hover=False,
                                                   command=self.github_link,
                                                   width=30)
        self.image_label.grid(column=3, row=3)

    def button_callback(self):
        try:
            self.filename = askopenfilename(
                filetypes=[('XML спектр', '*.xml'), ('CSV спектр', '*.csv')],
                title='Выберите спектр в формате .xml или .csv'
            )
            if self.filename:
                path_to_file = self.filename
                self.button.configure(text=path_to_file.split('/')[-1])
                self.button1.configure(state=NORMAL)
            else:
                print('Файл не выбран')
        except Exception as e:
            print('Произошла ошибка:', str(e))

    def converting(self):
        try:
            print('Конвертация')
        except Exception as e:
            print('Произошла ошибка:', str(e))

    def github_link(self):
        try:
            webbrowser.open('https://github.com/byBenPuls/spectrumconverter')
        except Exception as e:
            print('Произошла ошибка:', str(e))
