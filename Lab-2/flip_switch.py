class switch:
 def __init__(self, name, key):
  self.state = 0
  self.name = name
  self.key = key

 def flip(self):
  self.state = (self.state + 1) % 2