import tkinter as tk

#variables
WHITE = "#F8F8F8" # black/white
OP_COLOR = "#F1EABC" # black/tan
var = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}
#variables

#main layout
window = tk.Tk()
window.title('CrossRoads')
window.config(bg='#272533')

display_text = tk.StringVar()
display_text.set('0.0000')

background = tk.Canvas(bg="#F8F8F8", bd=0, highlightthickness=0)
background.pack(padx=15, pady=15)

tk.Label(background, text='CrossRoads', anchor='e', bg='#272533', fg='white', font=('Franklin Gothic Book', 14, 'bold')).grid(row=0, columnspan=4, sticky='ew', padx=4, pady=2)
tk.Label(background, textvariable=display_text, anchor='e', bg='#C0C0C0', fg='black', font=('Digital-7',47)).grid(row=1, columnspan=4, sticky='ew', padx=4, pady=2)
#main layout

#button layout
def std_btn(text, bg, row, col, width=7, height=2, font=('Franklin Gothic Book', 24)):
    btn = tk.Button(background, text=text, bg=bg, width=width, height=height, font=font, command=lambda: event_click(text))
    return btn.grid(row=row, column=col, padx=4, pady=4)

std_btn("C", OP_COLOR, 2, 0),   std_btn("CE", OP_COLOR, 2, 1),  std_btn("%", OP_COLOR, 2, 2),   std_btn("/", OP_COLOR, 2, 3)
std_btn("7", WHITE, 3, 0), std_btn("8", WHITE, 3, 1), std_btn("9", WHITE, 3, 2), std_btn("*", OP_COLOR, 3, 3)
std_btn("4", WHITE, 4, 0), std_btn("5", WHITE, 4, 1), std_btn("6", WHITE, 4, 2), std_btn("-", OP_COLOR, 4, 3)
std_btn("1", WHITE, 5, 0), std_btn("2", WHITE, 5, 1), std_btn("3", WHITE, 5, 2), std_btn("+", OP_COLOR, 5, 3)
std_btn("0", WHITE, 6, 0), std_btn(".", WHITE, 6, 1)

rtn_btn = tk.Button(background, text='=', bg='#C0C0C0', width=15, height=2, font=('Franklin Gothic Book', 24), command=lambda: event_click("="))
rtn_btn.focus()
rtn_btn.grid(row=6, column=2, columnspan=2, padx=4, pady=4)
#button layout



window.mainloop()