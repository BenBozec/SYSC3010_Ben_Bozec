from sense_hat import SenseHat
import time

sense = SenseHat()

blue = (0, 0, 255)
red = (255, 0, 0)


def update_screen(mode):
  if mode == "first_initial":
    sense.show_letter("T", back_colour = blue)

  elif mode == "second_initial":
    sense.show_letter("A", back_colour = red)


index = 0
initials = ["first_initial", "second_initial"]

update_screen("first_initial")

while True:
  selection = False
  events = sense.stick.get_events()
  for event in events:
    # Skip releases
    if event.action != "released":
      if event.direction == "left":
        index -= 1
        selection = True
      elif event.direction == "right":
        index += 1
        selection = True
      elif event.direction == "down":
        index -= 1
        selection = True
      elif event.direction == "up":
        index += 1
        selection = True
      if selection:
        current_mode = initials[index % 3]
        update_screen(current_mode)
  