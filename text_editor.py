# Text Editor in Python

from tkinter import*
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Izhan - TextPad!')
# root.iconbitmap('c:/gui/izhan.ico')
root.geometry("1200x660")

# Create New File Function
def new_file():
    # Delete Previous text
    my_text.delete("1.0", END)
    # Update status bars
    root.title('New File - TextPad!')
    status_bar.config(text="New File      ")

# Open Files
def open_file():
    # Delete Previous text
    my_text.delete("1.0", END)

    # Grab Filename
    text_file =filedialog.askopenfilename(initialdir="C", title="Open File", filetypes=(("Text Files", "*.txt"),("HTML Files", "*html"), ("Python Files","*,py"),("All Files", "*.*")))
    name = text_file
    status_bar.config(text=f'{name}    ')
    name = name.replace("C","")
    root.title(f'{name} - TextPad!')

    # Open File
    text_file = open(text_file,'r')
    stuff = text_file.read()
    # Add File to textbox
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()


# save_as_file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C", title="Save File", filetypes=(("Text Files")))
    if text_file:
        # Update status Bar
        name = text_file
        status_bar.config(text=f'{name}    ')
        name = name.replace("C")
        root.title(f'{name} - TeextPad!')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # close the file
        text_file.close()

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=save_as_file)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar TO Buttom of App
status_bar = Label(root, text='Ready   ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

#Loop!

root.mainloop()