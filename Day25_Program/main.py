import turtle 
import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.title("US_States Game")
screen.addshape(image)


turtle1 = turtle.Turtle()
turtle1.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
x_cor_states = data["x"].to_list()
y_cor_states = data["y"].to_list()

def check_answer():
        if answer in all_states:
            turtle2 = turtle.Turtle()
            turtle2.hideturtle()
            turtle2.penup()
            print("You guessed the state correctly")
            correct_guess = data[data["state"] == answer]
            turtle2.goto(int(correct_guess.x),int(correct_guess.y))
            turtle2.write(answer)
            game_states.append(answer)
                # print(correct_guess["x"], correct_guess["y"])
                # turtle2.goto(correct_guess["x"],correct_guess["y"])
game = 0
game_states = []
while game < 51:
    answer = screen.textinput(title=f" {game}/50, Guess the US State", prompt="What's another state name?")
    check_answer()
    game+= 1
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in game_states:
                missing_states.append(state)
        print(missing_states)
        new_frame = pandas.DataFrame(missing_states)
        new_frame.to_csv("states_to_learn")
        break
    

screen.mainloop()

