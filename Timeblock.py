class Timeblock:
  """
  The Timeblock class is a node-type class for creating the daily structure of the Schedule data structure.
  """

  def __init__(self, time: str):
    """
    Creates a Timeblock object with no assigned Employee. Each block represents 15 minutes of time, starting at the 
    time entered.
    
    Each Timeblock will link to a previous Timeblock or Weekday (prev), a next Timeblock (next), and is linked to a 
    sister shift (sister) that has the same time value, but different employee and shift values.

    :param time: The start of the fifteen minute block of time the Timeblock represents. Format should be "HH:MMam" or 
                 "HH:MMpm".
    :param type: string
    """
    self.time = time
    self.employee = "None Set"
    self.shift = "None Set"
    self.next = "None Set"
    self.prev = "None Set"
    self.sister = "None Set"

  def __repr__(self):
    """
    Generates and returns a string representation of the Timeblock object for printing.
    
    :return: Basic information about the Timeblock.
    :rtype: string
    """
    if self.shift == "None Set":
      shift = "Not Specified"
    else:
      shift = self.shift
    if self.employee == "None Set":
      employee = "Not Scheduled"
    else:
      employee = self.employee
    if self.sister == "None Set":
      sister = "Not Scheduled"
    elif self.sister.employee == "None Set":
      sister = "Not Scheduled"
    else:
      sister = self.sister.employee

    return f"{self.time}\nShift: {shift}\nEmployee: {employee}\nSister Shift: {sister}"

  def set_employee(self, employee:"Employee"):
    """
    Sets or updates the Employee scheduled to work in the Timeblock.

    :param employee: The Employee being assigned to the Timeblock.
    :param type: Employee object.
    """
    self.employee = employee
  
  def set_shift(self, shift: int) -> bool:
    """
    Sets which shift the Timeblock is aligned with to link further Timeblocks with.

    :param shift: The number of the shift, which should be either 1 or 2.
    :param type: integer
    :return: True if the shift was set, False if there is already a shift number assigned.
    :return type: boolean
    """
    if self.shift == "None Set":
      self.shift = shift
      return True
    else:
      return False

  def set_next(self, next: "Timeblock") -> bool:
    """
    Sets up a link to the next Timeblock in the shift.

    :param next: The next Timeblock to add to the shift.
    :param type: Timeblock object.
    :return: True if the Timeblock was assigned as next, False if there is already a Timeblock assigned to the current's 
             next.
    :return type: boolean
    """
    if self.next == "None Set":
      self.next = next
      return True
    else:
      return False

  def set_prev(self, previous: "Timeblock") -> bool:
    """
    Sets up a link to the previous Timeblock in the shift.

    :param previous: The previous Timeblock to link to the current.
    :param type: Timeblock object.
    :return: True if the Timeblock was assigned as previous, False if there is already a Timeblock assigned as the 
             current's previous.
    :return type: boolean
    """
    if self.prev == "None Set":
      self.prev = previous
      return True
    else:
      return False

  def set_sister(self, sister: "Timeblock") -> bool:
    """
    Sets up a link to the sister Timeblock in the alternate shift.

    :param sister: A Timeblock in the alternate shift to link to the current.
    :param type: Timeblock object.
    :return: True if the Timeblock was assigned as sister, False if there is already a Timeblock assigned as the 
             current's sister.
    :return type: boolean
    """
    if self-sister == "None Set":
      self.sister = sister
      return True
    else:
      return False
