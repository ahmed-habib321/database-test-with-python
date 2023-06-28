from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Tools.Design import *




def msg(message):
    messagebox.showinfo("Error",message)  


def dye(form, Red, Green, blue):
    form.config(background="#%s%s%s" % (Red, Green, blue))


def make_space(frame: Tk, size: int):
    Label(frame, text=" ", font=("", size), background=frame["bg"]).pack()


def strVar(value=""):
    return StringVar(value=value)


def intVar(value = 0):
    return IntVar(value=value)


def boolVar(value=False):
    return BooleanVar(value=value)


def digits(text):
    return (str.isdigit(text)) or (text == '')


def form(height, Title="", is_center=True,  width=0):
    f = Tk()
    f.title(Title)
    f.resizable(False,False)
    if width == 0:
        f.geometry("%dx%d" % (height, height))
    else:
        f.geometry("%dx%d" % (width, height))
    if is_center:
        center(f)
        return f

def Toplvl(height, Title="", is_center=True,  width=0):
    f = Toplevel()
    f.title(Title)
    if width == 0:
        f.geometry("%dx%d" % (height, height))
    else:
        f.geometry("%dx%d" % (width, height))
    if is_center:
        center(f)
        return f

def frame(form, bg=None):
    if bg != None:
        return Frame(form, bg=bg)
    else:
        return Frame(form)


def button(form, text=' Button ', command=None):
    btn = ttk.Button(form, text=text)
    if command != None:
        btn.config(command=command)
    return btn


def label(form, text='Label'):
    return ttk.Label(form, text=text)


def textbox(form, variable=None, is_number_only=False , read_only = False):
    reg = form.register(digits)
    txt = ttk.Entry(form)
    if is_number_only:
        txt.config(validate='key', validatecommand=(reg, "%P"))
    if variable != None:
        txt.config(textvariable=variable)
    if read_only:
        txt.config(state="readonly")
    return txt

def passwordbox(form, variable=None):    
    txt = textbox(form=form,variable=variable,is_number_only=False,read_only = False)
    txt.config(show="•")
    return txt

def radio(form, text='Radio', value=0, variable=None):
    rdo = ttk.Radiobutton(form, text=text, value=value)
    if variable != None:
        rdo.config(variable=variable)
    return rdo


def checkbox(form, text=' CheckBox ', variable=None):
    cbx = ttk.Checkbutton(form, text=text)
    if variable != None:
        cbx.config(variable=variable)
    return cbx


def combobox(form, values=None, readonly=False):
    cbx = ttk.Combobox(form)
    if values != None:
        cbx.config(values=values)
    if readonly:
        cbx.config(state='readonly')
    return cbx


def listbox(form, values=None):
    lbx = Listbox(form)
    if values != None:
        i = 0
        for x in values:
            lbx.insert(i, x)
            i += 1
    return lbx


def center(form: Tk):
    form.update()
    fw = form.winfo_width()
    fh = form.winfo_height()
    sw = form.winfo_screenwidth()
    sh = form.winfo_screenheight()
    X = (sw - fw) / 2
    y = (sh - fh) / 2
    form.geometry('%dx%d+%d+%d' % (fw, fh, X, y))


def bgall(form: Tk, bg):
    form.update()
    ctrls = form.winfo_children()
    form.config(bg=bg)
    for c in ctrls:
        ci = str(c.winfo_class()).strip()
        if ci == 'Frame':
            bgall(c, bg)
        if ci == 'Label' or ci == 'Button' or ci == 'Entry' or ci == 'Radiobutton':
            c['bg'] = bg
        if ci == 'TLabel' or ci == 'TButton' or ci == 'TEntry' or ci == 'TRadiobutton' or ci == 'TCheckbutton' or ci =="TFrame":
            my = ttk.Style()
            my.configure('TLabel', background=bg)
            my.configure('TButton', background=bg)
            my.configure('TEntry', background=bg)
            my.configure('TFrame', background=bg)
            my.configure('TRadiobutton', background=bg)
            my.configure('TCheckbutton', background=bg)


def fgall(form, fg):
    form.update()
    ctrls = form.winfo_children()
    for c in ctrls:
        ci = str(c.winfo_class()).strip()
        if ci == 'Frame':
            fgall(c, fg)
        if ci == 'Label' or ci == 'Button' or ci == 'Entry' or ci == 'Radiobutton':
            c['fg'] = fg
        if ci == 'TLabel' or ci == 'TButton' or ci == 'TEntry' or ci == 'TRadiobutton' or ci == 'TCheckbutton':
            my = ttk.Style()
            my.configure('TLabel', foreground=fg)
            my.configure('TButton', foreground=fg)
            my.configure('TEntry', foreground=fg)
            my.configure('TCheckbutton', foreground=fg)


def fontall(form, font):
    form.update()
    ctrls = form.winfo_children()
    for c in ctrls:
        ci = str(c.winfo_class()).strip()
        if ci == 'Frame':
            fontall(c, font)
        if ci == 'Label' or ci == 'Button' or ci == 'Entry' or ci == 'Radiobutton' or ci == 'TEntry':
            c['font'] = font
        if ci == 'TLabel' or ci == 'TButton' or ci == 'TRadiobutton' or ci == 'TCheckbutton':
            my = ttk.Style()
            my.configure('TLabel', font=font)
            my.configure('TButton', font=font)
            my.configure('TRadiobutton', font=font)
            my.configure('TCheckbutton', font=font)

def justifyall(form, justify):
    form.update()
    ctrls = form.winfo_children()
    for c in ctrls:
        ci = str(c.winfo_class()).strip()
        if ci == 'Frame':
            justifyall(c, justify)
        if ci == 'Entry':
            c['justify'] = justify
        if  ci == 'TEntry':
            c.config(justify=justify)
            


def check(txt: Entry, f: Toplevel, sv: StringVar):
    if (txt.get().strip() == ""):
        messagebox.showwarning("warning", "you have not entered any thing")
        sv.set("")
        txt.focus()
    else:
        f.destroy()


def inbox(text: str, numberonly=False):
    f = Toplevel()
    f.title(text)
    f.geometry(str(INW)+"x"+str(INH))
    f.resizable(False, False)
    center(f)
    ttk.Label(f, text=text, font=FONT , background="#EEEEEE" , foreground="black").pack(pady=10)
    sv = StringVar()
    txt = ttk.Entry(f, font=FONT, width=35, textvariable=sv, foreground="black")

    if numberonly:
        reg = f.register(digits)
        txt.config(validate='key', validatecommand=(reg, "%P"))

    txt.pack(pady=10)
    txt.bind('<Return>', lambda my: check(txt, f, sv))
    ttk.Style().configure('in.TButton', font=FONT)
    ttk.Button(f, text=' OK ', command=lambda: check(
        txt, f, sv), style="in.TButton").pack(pady=10)
    f.grab_set()
    txt.focus()
    f.wait_window()
    return sv.get()


def Table(Frame,Header,Matrix:list , evencolor , oddcolor):
    ttk.Style().configure("odd.TLabel" ,background=oddcolor , width=WIDTH, foreground = "black")
    ttk.Style().configure("even.TLabel" ,background=evencolor , width=WIDTH , foreground = "black")
    Matrix.insert(0,Header)
    Table = ttk.Frame(Frame)
    for i in range(len(Matrix)):

        q = label(Table , "")        
        if (i+1)%2!=0:
            q.config(style="odd.TLabel")
        else:
            q.config(style="even.TLabel")
        q.grid(row=i,column=0 , columnspan=len(Matrix[0]) ,sticky="nswe" , padx=PAD1 )


        for j in range(len(Matrix[0])):
            q = label(Table , Matrix[i][j])
            if (i==0):
                q.config(style="odd.TLabel", foreground="navy")
            if (i+1)%2!=0:
                q.config(style="odd.TLabel")
            else:
                q.config(style="even.TLabel")
            q.grid(row=i,column=j , padx=PAD1)
    
    return Table


def askbox(text: str):    
    return messagebox.askyesno(title="Alert",message=text)