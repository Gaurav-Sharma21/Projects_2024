# Password Manager App
# UI for this 
from tkinter import *
from tkinter import messagebox
import random
import json


#Window for the program
window = Tk()
window.title("Password Generator/Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image= lock_image)
canvas.grid(row=0,column=1)

#Password Generator 
def gen_pass():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  letter_list = [random.choice(letters) for _ in range(nr_letters)]
  symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
  number_list = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = letter_list + symbol_list + number_list

  random.shuffle(password_list)

  final_password = "".join(password_list)
  password_field.insert(0, final_password)


    

#Saving the data 
def add_save():
    website_value = website_field.get()
    email_value = email_field.get()
    password_value = password_field.get()
    new_data = {website_value: {
        "email": email_value,
        "password": password_value
    }}

    if len(website_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json","r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json","w") as f:
                json.dump(new_data,f, indent=4)
        else:
            data.update(new_data)

            with open("data.json","w") as f:
                json.dump(data,f, indent=4)
    
            website_field.delete(0,END)
            password_field.delete(0,END)

#Searching from the File to find 
def find_password():
    website_value_one = website_field.get()
    try:
        with open("data.json","r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data file found")
    else:
        if website_value_one in data:
            email = data[website_value_one]["email"]
            password = data[website_value_one]["password"]
            messagebox.showinfo(title=website_value_one,message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showwarning(title="Error",message="No details for the said website. Please add them")

#Labels 
website_label = Label(text="Website:", fg="#9bdeac")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:", fg="#9bdeac")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:", fg="#9bdeac")
password_label.grid(column=0,row=3)

#Text_field
website_field = Entry(width=21)
website_field.grid(column=1,row=1)
website_field.focus()

email_field = Entry(width=35)
email_field.grid(column=1,row=2,columnspan=2)
email_field.insert(0,"gauravisthebest@godly.com")

password_field = Entry(width=21)
password_field.grid(column=1,row=3)

#Button 
add_button = Button(text="Add",width=36,command=add_save)
add_button.grid(column=1,row=4,columnspan=2)

password_button = Button(text="Generate Password",command=gen_pass)
password_button.grid(column=2,row=3) 

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1)


window.mainloop()


