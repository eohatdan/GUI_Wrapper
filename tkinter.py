from tkinter import  *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')
def quit_loop(self):
    quit()
def entry_return(self):
    content = entry.get()
    print(content)
def print_content():
    global entryb1
    content = entryb1.get()
    print(content)
def callback(event):
    global last_entry_text
    last_entry_text = last_entry.get()
    print("In callback(); text of last_entry = "+last_entry_text)
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("Using Dan's very excellent GUI Wrapper")
        self.geometry('500x300')
        
    def createFrame(self,root,**kwargs):
        frame = ttk.Frame(root)
        frame['borderwidth'] = 20
        frame['relief'] = 'sunken'
        
        frame.columnconfigure(0,weight=1)
        frame.columnconfigure(0,weight=3)
        return frame
        
    def addButton(self,root,**kwargs):
        filter_list = ['text','command'] # Only the keywords in filter_list allowed
        self.button = ttk.Button(self)
        for parm in kwargs:
            got_parm = kwargs.get(parm)
            if parm in filter_list:
                if parm == 'text': # Handle text= optional parm
                    self.button = ttk.Button(self,text=got_parm)
                if parm == 'command': # Handle command=  optional parm
                    target = got_parm.replace("'","")
                    self.button.bind("<Button-1>",eval(target))
            else:
                print("Unrecognized or unallowed key-word: "+parm)
    
    def addEntry(self,root,row,col,**kwargs):
        filter_list = ['bd','callback']
        self.entry = tk.Entry(self)
        #self.button = Button(self,text=blabel,command=self.on_button)
        for parm in kwargs:
            got_parm = kwargs.get(parm)
            if parm in filter_list:
                if parm == 'bd':
                    # Incrementally change the Entry options.
                    self.entry.config(bd=got_parm)
                if parm == 'callback':
                    #self.entry.bind('<Return>',callback)
                    pass
            else:
                print("Unrecognized or unallowed key-word: "+parm)
                return
        self.entry= Entry(self)
        self.entry.grid(row=row,column=col)
        #self.button.grid()
        
        #self.entry.bind('<Return>',entry_return)
        return self.entry
    def on_button(self):
        print(self.entry.get())
    def addLabel(self,root,**kwargs):
        filter_list = ['text']
        self.label = tk.Label(self)
        for parm in kwargs:
            got_parm = kwargs.get(parm)
            if parm in filter_list:
                if parm == 'text':
                    # Incrementally change the Label options.
                    self.label.config(text=got_parm)
            else:
                print("Unrecognized or unallowed key-word: "+parm)
                
        
        return self.label
        
if __name__ == "__main__":
    # Create a new GUI app.
    app = App()
    # Create a new frame within the app.
    frame = app.createFrame(app,height=100, width= 100)
    # Add a button in the frame with 'button_clicked' as its callback
    app.addButton(frame,text='Click here',command='button_clicked')
    # Place the button in the next available spot in a grid.
    app.button.grid()
    # Add another button to the frame with command 'quit_loop'.
    # This will give the option to end the application when clicked.
    app.addButton(frame,text='Quit',command='quit_loop')
    # Place the button in the next row, column 5.
    app.button.grid(column=5)
    # Add a new label to the frame, and assign the Label object to label01.
    label01= app.addLabel(app,text="xxx")
    # Add submit button for entry
    last_entry_button = app.addButton(app,text='Submit')
    # Add a new entry to the frame, and return the client response to entry01.
    row=1;col=3
    last_entry = app.addEntry(frame,row,col,bd=5,callback="")
   
    # Assign the label, entry and button to the next available rows in the grid.
    app.label.grid()
    app.entry.grid()
    app.button.grid()
    app.bind('<Return>',callback)
    
    client_input = last_entry.get()
    print(client_input)
    app.mainloop()
    
