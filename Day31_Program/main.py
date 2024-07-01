# Flash card app capstone project 
# Using Tkinter 
from tkinter import *
import pandas as pd
import random

card = {}
COLOR_BACKGROUND = "#B1DDC6"
#Importing the csv to pandas dataframe
try:
    df = pd.read_csv("remaining_words.csv")
except FileNotFoundError:
    new_df = pd.read_csv("french_words.csv")
    new_dict = new_df.to_dict(orient="records")
# print(new_dict)
else:
    new_dict = df.to_dict(orient="records")


#Button Functions


def flip_card():
    canvas.itemconfig(language_text,text = "English",fill= "white")
    canvas.itemconfig(word_text, text = card["English"], fill = "white")
    canvas.itemconfig(card_image,image= card_back_image)

def already_finished():
    new_dict.remove(card)
    word_generator()
    data = pd.DataFrame(new_dict)
    data.to_csv("remaining_words.csv",index=False)



#Window for the program 
window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50, bg=COLOR_BACKGROUND)

time_var = window.after(3000,func=flip_card)

def word_generator():
    global card
    global time_var
    window.after_cancel(time_var)
    card = random.choice(new_dict)
    canvas.itemconfig(language_text,text = "French", fill= "black")
    canvas.itemconfig(word_text,text = f"{card['French']}",fill = "black")
    canvas.itemconfig(card_image,image= card_front_image)
    time_var = window.after(3000,func=flip_card)


canvas = Canvas(width=800,height=526)
card_front_image = PhotoImage(file = "card_front.png")
card_back_image = PhotoImage(file="card_back.png")
card_image = canvas.create_image(400,263, image= card_front_image)
language_text = canvas.create_text(400,150,text="French",fill="black",font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263,text="word",fill="black",font=("Ariel",60,"italic"))
canvas.config(bg=COLOR_BACKGROUND, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


#Buttons 
correct_image = PhotoImage(file= "right.png")
wrong_image = PhotoImage(file="wrong.png")
correct_button = Button(image=correct_image,highlightthickness=0, command=already_finished)
correct_button.grid(column=1,row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0,command=word_generator)
wrong_button.grid(column=0,row=1)


word_generator()



window.mainloop()