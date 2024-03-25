import customtkinter
from customtkinter import NORMAL
from tkinter.filedialog import askopenfilename
from PIL import Image
import webbrowser
import GUI.src.convertation.main as convertation
import GUI.src.temp.data as data


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

        self.button_select = customtkinter.CTkButton(self, text='Нажмите, чтобы выбрать файл',
                                                     command=self.button_callback,
                                                     anchor=customtkinter.CENTER
                                                     )
        self.button_select.grid(column=0, row=0)
        self.button_convertation = customtkinter.CTkButton(self, text='конвертировать',
                                                           border_width=1,
                                                           state=customtkinter.DISABLED,
                                                           fg_color='green',
                                                           hover_color='#005B00',
                                                           command=self.converting,
                                                           height=40,
                                                           anchor=customtkinter.CENTER)
        self.button_convertation.grid(column=0, row=1)

        self.github_image = customtkinter.CTkImage(Image.open('../resources/icons/github-mark-white.png'),
                                                   size=(30, 30))

        self.image_label = customtkinter.CTkButton(self, image=self.github_image, text='',
                                                   fg_color='transparent', hover=False,
                                                   command=self.github_link,
                                                   width=30)
        self.image_label.grid(column=2, row=2)

    def default_buttons(self):
        self.button_select.configure(text='Нажмите, чтобы выбрать файл')
        self.button_convertation.configure(
            text='конвертировать',
            state=customtkinter.DISABLED,
            fg_color='green',
            hover_color='#005B00',
        )

    def button_callback(self):
        try:
            self.default_buttons()
            self.filename = askopenfilename(
                filetypes=[('XML спектр', '*.xml'), ('CSV спектр', '*.csv')],
                title='Выберите спектр в формате .xml или .csv'
            )
            if self.filename:
                path_to_file = self.filename
                data.path_to_file = path_to_file
                data.filetype = path_to_file.split('/')[-1].split('.')[-1]
                self.button_select.configure(text=path_to_file.split('/')[-1])
                self.button_convertation.configure(state=NORMAL)
            else:
                print('Файл не выбран')
        except Exception as e:
            print('Произошла ошибка:', str(e))

    def converting(self):
        print('Конвертация')
        result = convertation.file_to_txt(data.path_to_file, filetype=data.filetype)
        if result:
            self.button_convertation.configure(fg_color='#896A05', text_color='white',
                                               text='Успешно!',
                                               state=customtkinter.DISABLED)

    def github_link(self):
        try:
            webbrowser.open('https://github.com/byBenPuls/spectrumconverter')
        except Exception as e:
            print('Произошла ошибка:', str(e))
