# UI for the Program 

from tkinter import *
import time
import math

reps = 0
timer = None



#CountDown mechanism 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_down,count - 1)
    else:
        start_program()
        marks = ""
        var_reps = math.floor(reps/2)
        for _ in range(var_reps):
            marks += "✔"
        label_two.config(text=marks)




window = Tk()
window.title("Pomodoro, Tomato in Italian")
window.config(padx=100,pady=50)


canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103,112,image= tomato_img)
canvas.grid(column=1,row=1)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=("Courier",30,"bold"))
canvas.grid(column=1,row=1)

#UI for the program
# It should have 3 buttons, start, pause and reset. 1 label to display the ticking time and one to show what to do when the timer buzzes


#Labels 
label_one = Label(text="TIMER", fg="#9bdeac")
label_one.grid(column=1,row=0)

label_two = Label(text="", fg="#9bdeac")
label_two.grid(column=1,row=3)

#Buttons 

def start_program():
    global reps
    reps += 1
    work_sec = 60 * 25
    break_sec = 60 * 5
    long_sec = 60 * 20
    if reps % 8 == 0:
        count_down(long_sec)
        label_one.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(break_sec)
        label_one.config(text="Short Break")
    else:
        count_down(work_sec)
        label_one.config(text="Timer")
    
# Reset Button, will reset everything to the beginning so we can start again 
def reset_timer():
    window.after_cancel(timer)
    label_one.config(text="Timer")
    label_two.config(text= "")
    canvas.itemconfig(timer_text,text = "00:00")
    global reps 
    reps = 0

button_one = Button(text="Start",command=start_program)
button_one.grid(column=0,row=2)


button_two = Button(text="Reset",command=reset_timer)
button_two.grid(column=2,row=2)




window.mainloop()
