import os
from tkinter import *

#Button Function
def button():
    current_value = taker.get()
    try:
        
        if int(current_value) > 100:
            label.config(text="You can't create more than 100 folders")
        else:
            for x in range(0, int(current_value)):
                os.mkdir(f"Folder {str(x)}")

    except ValueError:
        label.config(text="Please Enter A Number")
    except FileExistsError:
        label.config(text="This folder is existed. Please delete it before you try to make other one")
        
window = Tk()
#window stuff
window.geometry("500x500")
window.title("Folder Creator")
window.config(bg="#026e36")

#Label stuff
label = Label(text="You Are At " + os.getcwd(),
              font=("Arial", 20, 'bold'),
              fg='white',
              bg="#026e36")
label.pack()

#Input stuff
taker = Entry(width=20,
              font=("Arial", 30, 'bold'))
taker.insert(0,"Enter The Number")

taker.pack()

#Button stuff
button = Button(
    text="Submit",
    width=25,
    height=3,
    command=button
)
button.pack()

window.mainloop()


