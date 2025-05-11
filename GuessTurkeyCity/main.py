import turtle
import pandas as pd
import os

def get_high_score():
    if os.path.exists("data.txt"):
        with open("data.txt") as file:
            return int(file.read())
    else:
        return 0

def save_high_score(score):
    with open("data.txt", mode="w") as file:
        file.write(str(score))

def update_high_score(score):
    current_high = get_high_score()
    if score > current_high:
        save_high_score(score)
        print(f" New high score: {score}")
    else:
        print(f" Your score: {score} | High score: {current_high}")

def show_high_score():
    high_score = get_high_score()
    score_writer = turtle.Turtle()
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.goto(-300, 260)
    score_writer.color("black")
    score_writer.write(f"High Score: {high_score}", align="left", font=("Arial", 14, "bold"))

def check_state(answer_state, state_list, city):
    if answer_state in state_list:
        print(f'{answer_state} is in the state list.')
        state_list.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color('red')
        state_data = city[city.state == answer_state]
        x = float(state_data.iloc[0]['x'])
        y = float(state_data.iloc[0]['y'])
        t.goto(x, y)
        t.write(answer_state, align='center', font=('Arial', 8, 'normal'))

        if len(state_list) == 0:
            screen.textinput(
                title='WIN',
                prompt='YOU NAMED ALL 81 CITIES OF TURKEY!'
            )
            return False
        return True
    else:
        print(f'{answer_state} is not in the list.')
        return True

def answer_State_Name(state_list, city):
    number = len(state_list)
    answer_state = screen.textinput(
        title='Guess City',
        prompt=f'{81 - number}/81 - Enter a Turkish city name (or type "Exit" to quit):'
    )

    if answer_state is None or answer_state.lower() == 'exit':
        update_high_score(81 - number)
        return False

    answer_state = answer_state.title()
    return check_state(answer_state, state_list, city)
screen = turtle.Screen()
screen.title('Turkey City Guess Game')
image = 'turkiye_haritasi1.gif'
screen.addshape(image)
turtle.shape(image)
show_high_score()
city = pd.read_csv('81_States.csv')
state_list = city.state.tolist()
gameIsOn = True
while gameIsOn:
    gameIsOn = answer_State_Name(state_list, city)
screen.exitonclick()