#### GOAL ####
# Build a desktop app that it should allow a user to type and if they stop
# for more than 5 seconds, it should delete everything they've written so far.

from tkinter import *
import time

window = Tk()
window.geometry('1000x800')
window.title('The Most Dangerous Typing App')
window.config(bg="#A8DADC")
# Global variable to store last time user typed
last_typed_time = time.time()


def typing_timer():
    elapsed_time = time.time() - last_typed_time
    if elapsed_time > 5:
        user_input.delete(1.0, END) # delete from the 1st line, the zeroth character (starts counting from 0, by default)
    window.after(1000, typing_timer)

def reset_timer(event):
    global last_typed_time
    last_typed_time = time.time()

# Label
title = Label(text='The Most Dangerous Typing App 🤫', font=('Arial Bold', 40), bg='#A8DADC', fg='white', pady=30)
title.pack()
instructions = Label(text="Don't let your words fade away! \nKeep typing 💬 or lose everything"
                          " after 5 seconds!", font=('Arial', 30), bg='#A8DADC', justify='center', pady=20)
instructions.pack()

# Text - Box (multi-line)
user_input = Text(width=70,
    height=20,
    font=('Courier New', 16),
    wrap=WORD,
    bg="#fffefc",
    fg="#222",
    relief=FLAT,
    insertbackground="#444",  # cursor color
    padx=15,
    pady=15
)
user_input.pack(pady=20)

user_input.bind('<KeyRelease>', reset_timer)
typing_timer()

window.mainloop()