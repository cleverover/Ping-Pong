from tkinter import *

# Создаем необходимые функции: для выбора режима и для запуска того или иного режима
def play_australia():
    import australia

def play_classic():
    import classic

def get_option():
    button1.place_forget()
    introd.place_forget()               # Убираем старье
    anotation.place_forget()
    canvas.create_polygon(0, 240, 0, 300, 80, 300, fill='#646464')

    # Добавляем новые элементы: описания, заголовок, кнопки
    label_kek = Label(canvas, text = 'Ты на количество не смотри, они духом сильные', font=('arial', 16), fg = 'white', bg='#646464')
    label_kek.place(x= 5, y=10)

    button2 = Button(canvas, font=('arial', 15), text='Go!', fg='yellow', bg='green', command=play_australia)
    button3 = Button(canvas, font=('arial', 15), text='Go!', fg='black', bg='white', command=play_classic)

    australia_anotation1 = Label(canvas, text='Австралийский режим', font=('arial', 14), fg='yellow', bg='#646464')
    australia_anotation2 = Label(canvas, text = 'Твоя задача - сохранять мяч в игре! \n'
                                                'Иногда верх и низ будут меняться местами, \n'
                                                'Чтобы уловить момент, следи за нижней панелью.', font = ('arial', 11), fg = 'white', bg='#646464')
    classic_anotation1 = Label(canvas, text='Классический режим', font=('arial', 14), fg='#98ff98', bg='#646464')
    classic_anotation2 = Label(canvas, text='Твоя задача - забить 5 мячей. \n'
                                            'Периодически мяч будет ускоряться. \n'
                                            'Докажи, что ты разумнее бота!', font=('arial', 11), fg='white', bg='#646464')

    australia_anotation1.place(x=20, y=70)
    australia_anotation2.place(x=20, y=100)
    classic_anotation1.place(x=20, y=185)
    classic_anotation2.place(x=20, y= 215)
    button2.place(x=400, y=110)
    button3.place(x=400, y=230)

# Главное окно
root = Tk()
root.config(bg = '#646464')
root.geometry('500x300')
root.title('Понг-Пинг')
root.resizable(width=False, height=False)

# Холст
canvas = Canvas(root, width = 500, height = 300, bg = '#646464')
canvas.place(x = 0, y = 0)

# Стартовые виджеты: осписание, кнопка для выбора режима
introd = Label(canvas, text='Сайн Байна!', font=('arial', 30), fg='white', bg = '#646464')
introd.place(x = 130, y = 10)

anotation = Label(canvas, text = 'Я рад, что ты зашел, \n'
                                 'давай выберем игровой режим:', font = ('arial', 15), fg='white', bg = '#646464')
anotation.place(x=93, y=100)

button1 = Button(canvas, font = ('arial', 15), text = 'А давай', fg = 'black', bg = 'PeachPuff2', command = get_option)
button1.place(x = 188, y = 180)

# Немного графики, чтобы выглядело не так дешево
canvas.create_polygon(0, 240, 0, 300, 80, 300, fill = 'PeachPuff2')

root.mainloop()