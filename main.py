def on_button_pressed_a():
    global speed_left
    speed_left = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global speed_right
    speed_right = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

speed_left = 0
speed_right = 0
radio.set_group(1)
speed_right = 0
speed_left = 0

def on_forever():
    global speed_left, speed_right
    speed_left = Math.map(input.rotation(Rotation.ROLL), -90, 90, -1, 1)
    speed_right = Math.map(input.rotation(Rotation.ROLL), 90, -90, -1, 1)
    radio.send_value("speed_left", speed_left)
    radio.send_value("speed_right", speed_right)
    basic.show_number(speed_left)
    basic.pause(100)
basic.forever(on_forever)
