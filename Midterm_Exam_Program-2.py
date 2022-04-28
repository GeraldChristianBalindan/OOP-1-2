from tkinter import *
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400")

i = 1
def change_color():
    global i
    i += 1
    if i % 2 == 0:
        btn.configure(bg="Yellow")
    else:
        btn.configure(bg="White")


# Insert a Button Widget
btn = Button(window, text="Click to Change Color", bg="White", command=change_color)
btn.place(relx=.5, y=200, anchor="center")

window.mainloop()