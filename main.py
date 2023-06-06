def on_button_pressed_a():
    for index in range(4):
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
    basic.show_string("rojo")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index2 in range(4):
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
    basic.show_string("" + str(randint(rojo, azul)))
input.on_button_pressed(Button.B, on_button_pressed_b)

azul = ""
rojo = ""
rojo = "["rojo", "azul", "verde"]"
azul = "azul"

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
