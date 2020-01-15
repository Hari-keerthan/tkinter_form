from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('hello app')

def lab():
    name = Label(window, text='Name')
    name.grid(column=0,row=1)
    age = Label(window, text='Age')
    age.grid(column=0,row=2)
    roll = Label(window, text='Roll_no')
    roll.grid(column=0,row=3)
    sem = Label(window, text='Semester')
    sem.grid(column=0,row=4)

def only_numbers(char):
    return char.isdigit()

validation = window.register(only_numbers)
name_box = Entry()
name_box.grid(column=1,row=1)
age_box = Entry(window,validate="key", validatecommand=(validation, '%S'))
age_box.grid(column=1,row=2)
roll_box = Entry(window,validate="key", validatecommand=(validation, '%S'))
roll_box.grid(column=1,row=3)
sem_box = Entry()
sem_box.grid(column=1,row=4)
    

def onclick():
    a = str(name_box.get()) + ',' + str(age_box.get()) + ',' + str(roll_box.get()) + ',' + str(sem_box.get())
    print(a)
    f = open("file.csv","a+")
    f.write(a)
    f.close()
    messagebox.showinfo('sucess','successfully submitted!!!')

def clear_box():
    name_box.delete(0 , END)
    age_box.delete(0 , END)
    sem_box.delete(0 , END)
    roll_box.delete(0 , END)
    
lab()

submit = Button(window , text="submit" , command = lambda : onclick())
submit.grid(column=0,row=5)
clear = Button(window , text="clear" , command = lambda : clear_box())
clear.grid(column=1,row=5)
exi_t = Button(window , text="exit" , command = window.destroy)
exi_t.grid(column=2,row=5)
window.mainloop()
