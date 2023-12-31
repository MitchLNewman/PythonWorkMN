class Clock():
  def __init__(self, hours = 0, minutes = 0, seconds = 0):
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds

  def tick(self):
    self.seconds += 1
    if self.seconds == 60:
     self.minutes += 1
    if self.minutes == 60:
     self.hours += 1
    self.seconds %= 60
    self.minutes %= 60
    self.hours %= 24

  def __str__(self):
    return f"{'0' if self.hours < 10 else ''}{self.hours}:{'0' if self.minutes < 10 else ''}{self.minutes}:{'0' if self.seconds < 10 else ''}{self.seconds}"

class TwelveHourClock(Clock):
  def __init__(self, hours = 0, minutes = 0, seconds = 0, am = True):
    super().__init__(hours, minutes, seconds)
    self.am = am
  
  def tick(self):
    super().tick()
    if self.hours == 12:
      self.am = not self.am
    if self.hours > 12:
      self.hours %= 12
  
  def __str__(self):
    return super().__str__() + (" AM" if self.am else " PM")