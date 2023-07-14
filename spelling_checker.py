from textblob import TextBlob

from tkinter import *

def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0, END)
    enter2.insert(0, data)

def main_window():
    global enter1, enter2
    win = Tk()
    win.geometry("500x400")
    win.resizable(False, False)
    win.config(bg="aqua")
    win.title("Sumit Mahato")

    label1 = Label(win, text = "Incorrect Spelling" , font=("Time New Roman", 25, "bold"), bg="blue", fg="white")
    label1.place(x=100, y=20, height=50,width=300)

    enter1 = Entry(win,font=("Time New Roman", 25))
    enter1.place(x=100, y= 80 , height=50, width=300)

    label2 = Label(win, text="Correct Spelling", font=("Time New Roman", 25, "bold"), bg="blue", fg="white")
    label2.place(x=100, y=140, height=50, width=300)

    enter2 = Entry(win,font = ("Time New Roman", 25))
    enter2.place(x=100, y=200, height=50, width=300)

    button = Button(win, text="Done" ,font = ("Time New Roman", 25,"bold"), bg= "blue" , command=correct_spelling())
    button.place(x= 150, y = 280, height=50, width=200)


    win.mainloop()

main_window()
obj = TextBlob("data")
print(obj.correct())