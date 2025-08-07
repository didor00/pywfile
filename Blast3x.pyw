import tkinter
import customtkinter
import pymem

# Настройка основного окна
customtkinter.set_appearance_mode("Dark")
app = customtkinter.CTk()
app.geometry("700x300")
app.title("GITHUB.COM/BLAST3X | ЭТОТ ИНСТРУМЕНТ БЕСПЛАТНЫЙ")
app.resizable(False, False)

# Метка вверху
label_top = customtkinter.CTkLabel(master=app, text="СДЕЛАНО GITHUB.COM/BLAST3X", text_color="#FF0000")
label_top.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

# Метки для полей ввода
label_proc = customtkinter.CTkLabel(master=app, text="Имя процесса (например, notepad.exe):", text_color="#FFFFFF")
label_proc.place(relx=0.3, rely=0.2, anchor=tkinter.E)

label_addr = customtkinter.CTkLabel(master=app, text="Адрес памяти (hex, например, 0x10000000):", text_color="#FFFFFF")
label_addr.place(relx=0.3, rely=0.4, anchor=tkinter.E)

label_len = customtkinter.CTkLabel(master=app, text="Длина (например, 10):", text_color="#FFFFFF")
label_len.place(relx=0.3, rely=0.6, anchor=tkinter.E)

# Поля ввода
entry = customtkinter.CTkEntry(master=app, width=200, placeholder_text="notepad.exe")
entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

entry1 = customtkinter.CTkEntry(master=app, width=200, placeholder_text="0x10000000")
entry1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

entry2 = customtkinter.CTkEntry(master=app, width=200, placeholder_text="10")
entry2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Текстовое поле для результата
result_text = customtkinter.CTkTextbox(master=app, width=400, height=100)
result_text.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# Функция для кнопки
def button_event():
    procname = entry.get()
    address_str = entry1.get()
    length_str = entry2.get()

    # Проверка корректности ввода
    try:
        address = int(address_str, 16)  # Преобразование hex-адреса
        length = int(length_str)        # Преобразование длины
        if length <= 0:
            raise ValueError("Длина должна быть положительной")
    except ValueError as e:
        result_text.delete("1.0", tkinter.END)
        result_text.insert("1.0", f"Ошибка: Некорректный адрес или длина ({str(e)})")
        return

    # Работа с процессом
    try:
        pm = pymem.Pymem(procname)  # Открытие процесса
        rs = pm.read_string(address, length)  # Чтение строки
        rb = pm.read_bytes(address, length)   # Чтение байтов
        result_text.delete("1.0", tkinter.END)
        result_text.insert("1.0", f"Прочитанная строка: {rs}\nПрочитанные байты: {rb}")
    except Exception as e:
        result_text.delete("1.0", tkinter.END)
        result_text.insert("1.0", f"Ошибка: {str(e)}")

# Кнопка
button = customtkinter.CTkButton(master=app, text="Удалить строку", command=button_event)
button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

# Запуск приложения
app.mainloop()
