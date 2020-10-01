input.onButtonPressed(Button.A, function () {
    chosen = randint(1, 3)
    basic.showString("" + (countries[chosen]))
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(randint(1, 6))
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (capitals[chosen]))
})
// basic.show_string(datainfo[chosen_city])
input.onGesture(Gesture.Shake, function () {
    chosen_city = capitals[randint(0, 2)]
    basic.showString("" + (chosen_city))
    basic.pause(10000)
})
let chosen_city = ""
let chosen = 0
let capitals: string[] = []
let countries: string[] = []
countries = ["Canada", "Japan", "Peru"]
capitals = ["Ottawa", "Tokyo", "Lima"]
let datainfo = {
    "Canada" : "Ottawa",
    "Japan" : "Tokyo",
    "Peru" : "Lima",
}
