let x = 0
let y = 0
let c = 0
let d = 0
let e = 0
let f = 0

serial.redirectToUSB()
serial.setBaudRate(115200)

pins.setPull(DigitalPin.P12, PinPullMode.PullUp)
pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
pins.setPull(DigitalPin.P14, PinPullMode.PullUp)
pins.setPull(DigitalPin.P15, PinPullMode.PullUp)

basic.forever(function () {
    led.plot(0, 0)
    led.plot(4, 0)
    led.plot(0, 2)
    led.plot(0, 3)
    led.plot(1, 4)
    led.plot(2, 4)
    led.plot(3, 4)
    led.plot(4, 3)
    led.plot(4, 2)
    led.plot(2, 2)
    x = pins.analogReadPin(AnalogPin.P1)
    y = pins.analogReadPin(AnalogPin.P2)
    c = pins.digitalReadPin(DigitalPin.P12)
    d = pins.digitalReadPin(DigitalPin.P13)
    e = pins.digitalReadPin(DigitalPin.P14)
    f = pins.digitalReadPin(DigitalPin.P15)
    serial.writeNumbers([x, y, c, d, e, f])
    basic.pause(20)
})
