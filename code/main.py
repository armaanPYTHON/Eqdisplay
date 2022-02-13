from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from click import command
from numpy import pad
import txtopp as tp






def main_frontend(e=None):
    root = Tk()
    root.title('Eq Display')
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.config(bg='#212120')
    
    
    ## Main dictionary ------
    shortcutspath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Eq display/files/test/shortcuts.txt'
    namepath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Eq display/files/unicode_chart/symbol_name.txt'
    codepath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Eq display/files/unicode_chart/code.txt'
    names = tp.read_list(file=namepath, separator='\n')
    codes = tp.read_list(file=codepath, separator='\n')
    
    
    dict = {}
    
    for i in range(len(names)):
        dict[names[i]] = codes[i]


    displaybox = Text(root, font=('Arial', 13), bg='#5c5a5a', fg='white', bd=0)
    displaybox.place(relheight=0.9, relwidth=0.4, relx=0.05, rely=0.05)
    
    Label(root, text='Mathematical Symbol Name', fg='white', bg='#212120', font=("Arial", 15, 'italic')).place(relx=0.6, rely=0.05)
    entrybox = Entry(root, bd=0, font=("Arial", 15, 'italic'))
    entrybox.place(relwidth=0.4, relx=0.55, rely=0.1)
    
    file = filedialog.asksaveasfile(initialfile = 'Untitled.txt', 
                                        defaultextension=".txt",
                                        filetypes=[
                                            ("All Files","*.*"),
                                            ("Text Documents","*.txt")
                                            ]
                                        )
    global myfile
    try:
        myfile = file.name
    except:
        myfile = file
        
    
    def submit(e=None):
        value = entrybox.get()
        
        if value in names:
            entrybox.delete(0, END)
            displaybox.insert(END, dict[value])
        else:
            entrybox.delete(0, END)
            displaybox.insert(END, value)
    
    
    
    def clear():
        x = messagebox.askyesno('Clear Workspace', 'Are you sure you want to proceed with deleting your equations?')
        if x == 1:
            print('yes')
            displaybox.delete('1.0', END)
        else:
            pass
        
    def restart():
        root.destroy()
        main_frontend()
        
        
    def savefile(e=None):
        text = displaybox.get('1.0', END)
        tp.write(file=myfile, object=text.encode("utf8"))

        

    def openfile(e=None):
        global myfile
        myfile = filedialog.askopenfilename()
        text = tp.read_encoded(file=myfile)
        
        if displaybox.get('1.0', END) == '\n':
            displaybox.insert(END, text)
        
        else:
            x = messagebox.askyesno('Open File', 'The display box contains content.Do you wish to overwrite it?')
            if x == 1:
                displaybox.delete('1.0', END)
                displaybox.insert(END, text)
            else:
                displaybox.insert(END, text)

    
    
    def viewsymbol(e=None):
        win = Toplevel()
        win.title('Eq Display - Symbols')
        win.geometry('400x600')
        win.resizable(0,0)
        
        searchbox = Entry(win, width=30, bd=0, font=("Arial", 12))
        searchbox.pack(pady=20)
        
        lb = Listbox(win, height=30, width=50, bd=0)
        lb.pack()
        
        for i in range(len(codes)):
            lb.insert(END, str(codes[i])+' - '+str(names[i]))
            
        def search(e=None):
            value = searchbox.get().lower()
            
            items = []
            
            for i in range(len(codes)):
                items.append(str(codes[i])+' - '+str(names[i]))
            lb.delete(0, END)
            
            for item in items:
                if value == '':
                    lb.delete(0, END)
                    for i in range(len(codes)):
                        lb.insert(END, str(codes[i])+' - '+str(names[i]))
                elif value in item:
                    lb.insert(END, item)
                else:
                    pass
            
        searchbox.bind('<KeyRelease>', search)
        
        
    
    def addsymbol(e=None):
        win = Toplevel()
        win.title('Eq Display - Add Symbol')
        win.geometry('400x600')
        win.resizable(0,0)
        win.config(bg='#212120')
        
        Label(win, text='Name of Symbol: ', bg='#212120', fg='white').grid(row=0, column=0, padx=10, pady=10)
        Label(win, text='Symbol Character: ', bg='#212120', fg='white').grid(row=1, column=0, padx=10, pady=10)
        
        nameentry = Entry(win, width=30, bd=0)
        nameentry.grid(row=0, column=1, padx=10, pady=10)
        symbolentry = Entry(win, width=30, bd=0)
        symbolentry.grid(row=1, column=1, padx=10, pady=10)
        
        def symboladdsubmit(e=None):
            symbol = symbolentry.get()
            name = nameentry.get()
            
            symbolentry.delete(0, END)
            nameentry.delete(0, END)
            
            tp.add_object(file=namepath, separator='\n', object=name)
            tp.add_object(file=codepath, separator='\n', object=symbol)
            
        
        submitbtn = Button(win, bd=0, bg='white', text='Submit', command=symboladdsubmit)
        submitbtn.grid(row=2, column=0, columnspan=2, pady=10)
        
        win.bind('<Return>', symboladdsubmit)
        
        
    
    def shortcuts(e=None):
        value = tp.read_string(file=shortcutspath)
        
        win = Toplevel()
        win.title('Eq. Display - Shortcuts')
        win.resizable(0,0)
        win.geometry('200x150')
        win.config(bg='#212120')
        
        Label(win, text=value, bg='#212120', fg='white').pack()
    
    
    root.bind('<Control-o>', openfile)
    root.bind('<Control-s>', savefile)
    root.bind('<Return>', submit)
    root.bind('<Control-l>', addsymbol)
    root.bind('<Control-q>', viewsymbol)
    root.bind('<Control-n>', main_frontend)
    root.bind('<Control-c>', shortcuts)
    displaybox.bind('<KeyRelease>', savefile)

    
    #   FILE MENU
    menu = Menu(root)
    root.config(menu=menu)
    file = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=main_frontend)
    file.add_command(label='Save File', command=savefile)
    file.add_command(label='Open File', command=openfile)
    file.add_separator()
    file.add_command(label='Shortcuts', command=shortcuts)
    file.add_separator()
    file.add_command(label='Clear', command=clear)
    file.add_separator()
    file.add_command(label='Restart App', command=restart)
    file.add_command(label='Exit App', command=root.destroy)
    
    symbolmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Symbols', menu=symbolmenu)
    symbolmenu.add_command(label='View all Symbols', command=viewsymbol)
    symbolmenu.add_separator()
    symbolmenu.add_command(label='Add Symbol', command=addsymbol)
    
    mainloop()
    
main_frontend()