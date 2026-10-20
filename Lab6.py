# SED1115 - Lab 6: make the servo move
# Run this file ON THE PICO (MicroPico "Run" button in VS Code).
# The servo's orange wire must be connected to GP0.

from machine import Pin, PWM
import time


# This is the same translate function as in servo_translator.py
def translate(angle: float) -> int:
	# Step 1: Keep the angle between 0 and 180 degrees.
	if angle < 0:
		angle = 0
	if angle > 180:
		angle = 180

	# Step 2: Turn the angle into a pulse width (microseconds).
	pulse_width = 500 + (2500 - 500) * angle / 180

	# Step 3: Duty cycle = how much of the 20000 us period is "on" (0 to 1).
	duty_cycle = pulse_width / 20000

	# Step 4: Scale it to the 0-65535 range that duty_u16() uses.
	return int(duty_cycle * 65535)


# Set up the servo on GP0 at 50 Hz
servo = PWM(Pin(0))
servo.freq(50)

# Move the servo to 0, 90, 180, then back to 90, three times
for i in range(3):
	for angle in [0, 90, 180, 90]:
		print("Moving to", angle, "degrees")
		servo.duty_u16(translate(angle))
		time.sleep(1)    # wait 1 second so the servo has time to move

print("Done!")

