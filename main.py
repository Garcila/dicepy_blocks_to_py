def on_button_pressed_a():
    global chosen
    chosen = randint(1, 3)
    basic.show_string("" + (countries[chosen]))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(randint(1, 6))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("" + (capitals[chosen]))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global chosen_city
    chosen_city = capitals[randint(0, 2)]
    basic.show_string(chosen_city)
    basic.pause(10000)
    # basic.show_string(datainfo[chosen_city])
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

chosen_city = ""
chosen = 0
capitals: List[str] = []
countries: List[str] = []
countries = ["Canada", "Japan", "Peru"]
capitals = ["Ottawa", "Tokyo", "Lima"]
# unknown expression:  178
datainfo = {
    "Canada" : "Ottawa",
    "Japan" : "Tokyo",
    "Peru" : "Lima",
}