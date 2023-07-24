from piracer.vehicles import PiRacerStandard
from piracer.gamepads import ShanWanGamepad


if __name__ == '__main__' :

    shanwan_gamepad = ShanWanGamepad()
    piracer = PiRacerStandard()

    while True:
        gamepad_input = shanwan_gamepad.read_data()

        throttle = gamepad_input.analog_stick_left.y

        steering = gamepad_input.analog_stick_right.y

        print(f'throttle={throttle}, steering={steering}')

        piracer.set_throttle_percent(throttle * 0.5)
        piracer.set_steering_percent(steering)

