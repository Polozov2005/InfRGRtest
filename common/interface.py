from tkinter import *

root = Tk()
root.geometry("1080x720")



frm1 = Frame(root, background = '#abcdef', relief = SOLID, borderwidth = 1) 
frm1.place( x = 20, y = 20, width = 360, height = 300 )

frm2 = Frame(root, background = '#abcdef', relief = SOLID, borderwidth = 1) 
frm2.place( x = 0, y = 0, width = 360, height = 300 )

chk1 = Checkbutton( frm1, background = '#abcdef', font = ('Arial', 20))
chk1.grid(row = 0, column = 0)

root.mainloop()