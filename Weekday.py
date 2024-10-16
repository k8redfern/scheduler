class Weekday:
  """
  The Weekday class is another node-type class for creating the weekly structure of the Schedule data structure. Each
  Weekday object links to another Weekday object, and acts as a head for two linked lists of Timeblock objects (shifts).
  If a Weekday object is the start of a schedule, its previous field will remain set to None, and if it is the end of a
  Schedule, its next field will remain set to None.
  """

  def __init__(self, given_day: str):
    """
    Creates a Weekday object with no assigned Timeblocks or linked Weekdays.

    :param given_day: The name of the Weekday.
    :param type: string
    """
    self.day = given_day
    self.shift_1 = None
    self.shift_2 = None
    self.next_day = None
    self.prev_day = None

  def __repr__(self) -> str:
    """
    Generates and returns a string representation of the Weekday object for printing.

    :return: Basic information about the Weekday.
    :rtype: string
    """
    if self.next_day is None:
      next = "No Next Day Set"
    else:
      next = self.next_day.day
    if self.prev_day is None:
      previous = "No Prev Day Set"
    else:
      previous = self.prev_day.day
    if self.shift_1 is None:
      shift1 = "No Shift Set"
      shift1_time = "No Time Set"
    else:
      shift1 = self.shift_1.shift
    if self.shift_2 is None:
      shift2 = "No Shift Set"
      shift2_time = "No Time Set"
    else:
      shift2 = self.shift_2.shift
      shift2_time = self.shift_2.time
    
    return f"{self.day}:\nShift_1: {shift1}, Time: {shift1_time}\nShift_2: {shift2}, Time: {shift2_time}\nPrevious Day: {previous}\nNext Day: {next}"

  def set_shift(self, timeblock: "Timeblock") -> bool:
    """
    Sets a Timeblock as the first Timeblock node for either shift.

    :param timeblock: The Timeblock object to assign to a Weekday's first open shift.
    :param type: Timeblock object
    :return: True if the Timeblock was assigned to a shift, False if there are already Timeblocks assigned to both of
             the Weekday's shifts.
    :return type: boolean
    """
    if self.shift_1 is None:
      self.shift_1 = timeblock
      return True
    elif self.shift_2 is None:
      self.shift_2 = timeblock
      return True
    else:
      return False

  def set_next_day(self, next_weekday: "Weekday") -> bool:
    """
    Sets another Weekday as the current's next.

    :param next_weekday: The Weekday to set as the current's next_day.
    :param type: Weekday object
    :return: True if next_weekday was set as current's next_day, False if current's next_day already has a Weekday
             assigned.
    :return type: boolean
    """
    if self.next_day is None:
      self.next_day = next_weekday
      return True
    else:
      return False

  def set_prev_day(self, previous_weekday: "Weekday") -> bool:
    """
    Sets another Weekday as the current's prev_day. Will return False if current already has a prev_day set.

    :param previous_weekday: The Weekday to set as the current's prev_day.
    :param type: Weekday object
    :return: True if previous was set as current's prev_day, False if current's prev_day already has a Weekday assigned.
    :return type: boolean
    """
    if self.prev_day is None:
      self.prev_day = previous_weekday
      return True
    else:
      return False
