import turtle
import pandas as pd
from pathlib import Path
import csv

# Using pathlib, create relative paths for files in project
# Set relative path of the current script
current_dir = Path(__file__).parent

# Then use this to construct the path string to each file as referenced
## example: image = f"{current_dir}/images/file.gif"
## example: data_path = f"{current_dir}/data/file.csv" 


# TODO-1: Convert guess to Title case
# TODO-2: Check if guess is among the 50 states
# TODO-3: Write correct guesses onto the map
# TODO-4: Use loop to allow the user to keep guessing
# TODO-5: Record correct guesses in the list
# TODO-6: Keep track of the score

screen = turtle.Screen()
screen.title("US States Game")
image = f"{current_dir}/images/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(f"{current_dir}/data/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

states_left = all_states

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter State:").title()

    if answer_state == "Exit":
        missed_data = pd.DataFrame(states_left)
        missed_data.to_csv(f"{current_dir}/data/missed_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        states_left.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        t.goto(x_cor, y_cor)
        t.write(answer_state)

# Copy/pasted code below from stack overflow on getting mouse click coordinates (x/y)
# But this was already done to retrieve the x,y coordinates in 50_states.csv
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


screen.exitonclick()  # Removing this line to let us click on screen to derive coordinates


