import flip_switch
import keyboard #For reading keyboard inputs
import time

switch = flip_switch.switch("Switch A", "a")

while True:
	if keyboard.is_pressed(switch.key):
		switch.flip()
		if switch.state == 0:
			print(switch.name, "was turned off")
		if switch.state == 1:
			print(switch.name, "was turned on")
	time.sleep(0.2)
