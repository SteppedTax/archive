import os
import sys
filepath = (sys.argv[1])
if filepath.endswith('.libpr'):
    pass
else:
    sys.exit()
rfile = open(filepath, "r")
# rfile = open("default.libpr", "r")
rbook = rfile.read()
rfile.close()
list = rbook.split("\n")
listcount = (len(list) - 1)
page = ('')
pageid = 0

# pg1 = list[1] out of range
# for i in list:
#   print(i)

def prevPage():
    global pageid
    global page
    if pageid <= 0:
        page = (list[pageid])
        pagevar.set(page)
        window.mainloop()
        return
    else:
        pageid = (pageid - 1)
        page = (list[pageid])
        pagevar.set(page)
        window.mainloop()
def nextPage():
    global pageid
    global page
    if pageid < listcount:
        pageid = (pageid + 1)
        page = (list[pageid])
        pagevar.set(page)
        window.mainloop()
        return
    else:
        page == (list[pageid])
        pagevar.set(page)
        window.mainloop()
        return
def refreshPage():
    prevPage()
    nextPage()

# использую TKINTER.pyw за основу.
import tkinter as tkam
window = tkam.Tk()
window.title("v.1.4")
window.geometry("300x500")
window.resizable(False, False)

pagevar = tkam.StringVar()
# frame = tkam.Frame(window, width=500, height=55, bg='green')
# labelframe = tkam.LabelFrame(
#     window, 
#     text='')
textbox = tkam.Label(
    textvariable=pagevar,
    width=41,
    height=29,
    wraplength=290,    
    anchor='nw',
    justify='left',
    relief='sunken')
left = tkam.Button(
    text="<",
    command=prevPage,
    width=7,
    height=3)
right = tkam.Button( 
    text=">",
    command=nextPage,
    width=7,
    height=3)
# labelframe.pack(fill='both')
textbox.pack()
left.place(
    x=0,
    y=445)
right.place(
    x=240.5,
    y=445)
# left.pack(
#     side='bottom', 
#     anchor='sw') # тип меню - pack, place и grid
# right.pack(
#     side='bottom', 
#     anchor='se')
refreshPage()
window.mainloop()


# os.system("pause") # конец