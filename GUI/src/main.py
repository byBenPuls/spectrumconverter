import tkinter.messagebox
import webbrowser

import interface.view
import update.check
import update.compare
import update.load

VERSION = update.load.load_update()
new_version = update.check.check_update()

if __name__ == '__main__':
    app = interface.view.MainWindow()
    try:
        update_status = update.compare.compare_updates(VERSION, new_version)
        if update_status:
            pass
        else:
            update = tkinter.messagebox.askyesno(title='Spectrum Converter',
                                                 message=f'Доступно новое обновление (v{new_version}) программы.\n'
                                                         'Хотите установить обновление?')
            if update:
                webbrowser.open('https://github.com/byBenPuls/spectrumconverter/releases')
    except Exception as e:
        print('Update is not available {}'.format(e))
    app.mainloop()
