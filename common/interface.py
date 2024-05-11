from tkinter import *
from ctypes import windll

import initialization
import equation


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
    height = 160
)

frm_Y = Frame(
    root,
    background='yellow'
)
frm_Y.place(
    x=800,
    y=160,
    width = 800,
    height = 160
)

frm_E = Frame(
    root,
    background='green'
)
frm_E.place(
    x=800,
    y=320,
    width = 800,
    height = 160
)

frm_solveandsave = Frame(
    root,
    background='blue'
)
frm_solveandsave.place(
    x=800,
    y=480,
    width = 800,
    height = 100
)

frm_U = Frame(
    root,
    background='indigo'
)
frm_U.place(
    x=800,
    y=580,
    width = 800,
    height = 160
)

frm_X = Frame(
    root,
    background='violet'
)
frm_X.place(
    x=800,
    y=740,
    width = 800,
    height = 160
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
columncount_checkbutton = 0
for i in range(1, 24 +  1):
    if i == 9 or (11 < i < 21):
        list_label_checkbutton.append([])
        list_checkbutton.append([])
        list_enabled_checkbutton.append([])

    else:
        columncount_checkbutton += 1
        label_checkbutton = Label(
            frm_checkbutton,
            text=str(i)
        )

        list_label_checkbutton.append(label_checkbutton)

        list_label_checkbutton[i].grid(
            row = 0,
            column = columncount_checkbutton
        )

        enabled_checkbutton = IntVar(value=1)

        checkbutton = Checkbutton(
            frm_checkbutton,
            variable=enabled_checkbutton,
        )

        list_checkbutton.append(checkbutton)
        list_enabled_checkbutton.append(enabled_checkbutton)

        list_checkbutton[i].grid(
            row = 1,
            column = columncount_checkbutton,
        )

for i in range(columncount_checkbutton + 1):
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

for k in range(-((-len(Y_list)+1)//10)):
    label_i_Y = Label(
        frm_Y,
        text='i'
    )

    label_i_Y.grid(
        row=2*k,
        column=0,
    )

    label_Y = Label(
        frm_Y,
        text='Y[i], См'
    )

    label_Y.grid(
        row=2*k + 1,
        column=0,
    )

    for i in range(1, 10 + 1):
        label_count = Label(
            frm_Y,
            text=str(i + 10*k)
        )

        label_count.grid(
            row=2*k,
            column=i
        )

        delta = (len(Y_list) - 1) - 10*k
        if delta < 10:
            for j in range(1, delta + 1):
                label_Y_list = Label(
                    frm_Y,
                    text=str(Y_list[j + 10*k])
                )

                label_Y_list.grid(
                    row=2*k + 1,
                    column=j
                )

        else:
            label_Y_list = Label(
                frm_Y,
                text=str(Y_list[i + 10*k])
            )

            label_Y_list.grid(
                row=2*k + 1,
                column=i
            )

### Вывод кнопки для расчёта
def click_solve():
    A_matrix = initialization.A()['matrix']
    Y_matrix = initialization.Y()['matrix']
    I_matrix = initialization.I()['matrix']
    E_matrix = initialization.E()['matrix']

    if list_enabled_checkbutton[1].get() == 0:
        i = 5
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[2].get() == 0:
        i = 6
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[3].get() == 0:
        i = 9
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[4].get() == 0:
        i = 10
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[5].get() == 0:
        i = 13
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[6].get() == 0:
        i = 14
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[7].get() == 0:
        i = 15
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[8].get() == 0:
        i = 16
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[10].get() == 0:
        i = 30
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[11].get() == 0:
        i = 29
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[21].get() == 0:
        i = 7
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[22].get() == 0:
        i = 8
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[23].get() == 0:
        i = 21
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[24].get() == 0:
        i = 22
        Y_matrix[i - 1, i - 1] = 0

    U_list = equation.U(
        A=A_matrix,
        Y=Y_matrix,
        I=I_matrix,
        E=E_matrix
    )['list']

    X_list = equation.X(U_list)['list']

    print(U_list)
    # print(X_list)

btn_solve = Button(
    frm_solveandsave,
    text='Рассчитать',
    command=click_solve
)
btn_solve.grid(row=0, column=0)




root.mainloop()