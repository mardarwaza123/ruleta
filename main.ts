input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
    basic.showString("rojo")
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
    basic.showString("" + randint(rojo, azul))
})
let azul = ""
let rojo = ""
rojo = "rojo"
azul = "azul"
basic.forever(function () {
	
})
basic.forever(function () {
	
})
