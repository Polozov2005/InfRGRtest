from tkinter import *
from ctypes import windll
import initialization

# Настройка дизайна
background_color = '#181818'
foreground_color = '#cccccc'
widget_background_color = '#1f1f1f'
theme_color = '#4a9cd6'
font = 'Arial'

windll.shcore.SetProcessDpiAwareness(1) # Для отсутствия размытия интерфейса
root = Tk()
root.geometry("1600x900")
root.title("РГР")
root.resizable(False, False)
root.configure(bg=background_color)

frm_scheme = Frame(
    root,
    background='red'
)
frm_scheme.place(
    x=0,
    y=0,
    width = 800,
    height = 900
)

frm_checkbutton = Frame(
    root,
    background='orange'
)
frm_checkbutton.place(
    x=800,
    y=0,
    width = 800,
    height = 150
)

frm_Y = Frame(
    root,
    background='yellow'
)
frm_Y.place(
    x=800,
    y=150,
    width = 800,
    height = 150
)

frm_E = Frame(
    root,
    background='green'
)
frm_E.place(
    x=800,
    y=300,
    width = 800,
    height = 150
)

frm_solveandsave = Frame(
    root,
    background='blue'
)
frm_solveandsave.place(
    x=800,
    y=450,
    width = 800,
    height = 150
)

frm_U = Frame(
    root,
    background='indigo'
)
frm_U.place(
    x=800,
    y=600,
    width = 800,
    height = 150
)

frm_X = Frame(
    root,
    background='violet'
)
frm_X.place(
    x=800,
    y=750,
    width = 800,
    height = 150
)

### Выключатели

label_i_checkbutton = Label(
    frm_checkbutton,
    text='i'
)

label_i_checkbutton.grid(
    row=0,
    column=0,
)

label_B_checkbutton = Label(
    frm_checkbutton,
    text = 'B[i]'
)

label_B_checkbutton.grid(
    row=1,
    column=0,
)

list_label_checkbutton = [[]]
list_checkbutton = [[]]
list_enabled_checkbutton = [[]]
for i in range(1, 10 +  1):    
    label_checkbutton = Label(
        frm_checkbutton,
        text=str(i)
    )

    list_label_checkbutton.append(label_checkbutton)

    list_label_checkbutton[i].grid(
        row = 0,
        column = i
    )

    enabled_checkbutton = IntVar()

    checkbutton = Checkbutton(
        frm_checkbutton,
        variable=enabled_checkbutton,
    )

    list_checkbutton.append(checkbutton)
    list_enabled_checkbutton.append(enabled_checkbutton)

    list_checkbutton[i].grid(
        row = 1,
        column = i,
    )


for i in range(len(list_label_checkbutton)):
    frm_checkbutton.columnconfigure(
        index=i,
        weight=1
    )

for i in range(1 + 1):
    frm_checkbutton.rowconfigure(
        index=i,
        weight=1
    )

### Y
Y_list = initialization.Y()['list']

label_i_Y = Label(
    frm_Y,
    text='i'
)

label_i_Y.grid(
    row=0,
    column=0,
)

label_i_Y = Label(
    frm_Y,
    text='i'
)

label_i_Y.grid(
    row=2,
    column=0,
)

label_Y = Label(
    frm_Y,
    text='Y[i], См'
)

label_Y.grid(
    row=1,
    column=0,
)

for i in range(1, len(Y_list)):
    label_count = Label(
        frm_Y,
        text=str(i)
    )

    label_count.grid(
        row=0,
        column=i
    )

    label_Y_list = Label(
        frm_Y,
        text=str(Y_list[i])
    )

    label_Y_list.grid(
        row=1,
        column=i
    )

root.mainloop()