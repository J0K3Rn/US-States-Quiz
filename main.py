import turtle
import pandas

# Used for getting coordinates on map
# def get_mouse_click_coor(x, y):
#     print(x, y)


def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    correct = 0

    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.speed("fastest")

    data = pandas.read_csv("50_states.csv")
    states = data["state"].to_list()
    x_cor = data["x"].to_list()
    y_cor = data["y"].to_list()

    guessed_states = []
    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name?")

        if answer_state.title() == "Exit":
            # Add un-guessed states to list
            states_to_learn = [state for state in states if state not in guessed_states]
            states_to_learn_df = pandas.DataFrame(states_to_learn, columns=['states'])
            states_to_learn_df.to_csv('states_to_learn.csv')
            break

        for i, state in enumerate(states):
            if answer_state.upper() == state.upper():
                guessed_states.append(state)
                correct += 1
                writer.goto(int(x_cor[i]), int(y_cor[i]))
                writer.write(state)

    # Used for getting coordinates on map
    # turtle.onscreenclick(get_mouse_click_coor)
    # turtle.mainloop()


if __name__ == "__main__":
    main()
