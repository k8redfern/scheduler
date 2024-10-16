class Employee:
  """
  The Employee class has fields to hold each Employee's basic information for scheduling purposes, including their name
  and their availability. This class provides the methods to set or update their name, availability, maximum number of 
  shifts they wish to work each week, and whether they will accept working split shifts.
  """

  def __init__(self, name: str):
    """
    Creates an Employee object with default values and 100% availability.

    :param name: The actual name of the Employee. This will be used in the Schedule class and should be unique among
                 Employees.
    :param name: string
    """
    self.name = name
    self.splits = False
    self.max_shifts = 0
    self.priority = 0
    self.availability = {"Monday": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                         "Tuesday": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                         "Wednesday": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                         "Thursday": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                         "Friday": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                         "Saturday": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                      1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                         "Sunday": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                                    1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]}
    self.times = ["5:45am", 
                  "6:00am", "6:15am", "6:30am", "6:45am", 
                  "7:00am", "7:15am", "7:30am", "7:45am", 
                  "8:00am", "8:15am", "8:30am", "8:45am", 
                  "9:00am", "9:15am", "9:30am", "9:45am", 
                  "10:00am", "10:15am", "10:30am", "10:45am", 
                  "11:00am", "11:15am", "11:30am", "11:45am", 
                  "12:00pm", "12:15pm", "12:30pm", "12:45pm", 
                  "1:00pm", "1:15pm", "1:30pm", "1:45pm", 
                  "2:00pm", "2:15pm", "2:30pm", "2:45pm", 
                  "3:00pm", "3:15pm", "3:30pm", "3:45pm", 
                  "4:00pm", "4:15pm", "4:30pm", "4:45pm", 
                  "5:00pm", "5:15pm", "5:30pm", "5:45pm", 
                  "6:00pm", "6:15pm", "6:30pm", "6:45pm", 
                  "7:00pm", "7:15pm", "7:30pm", "7:45pm", 
                  "8:00pm", "8:15pm", "8:30pm", "8:45pm", 
                  "9:00pm", "9:15pm", "9:30pm", "9:45pm", 
                  "10:00pm", "10:15pm"]

  def __repr__(self) -> str:
    """
    Generates and returns a string representation of the Employee object for printing.
    
    :return: The Employee's name.
    :rtype: string
    """
    return self.name

  def set_name(self, new_name: str):
    """
    Updates the Employee name. Use when necessary to update the Employee's name to a more unique version, such as a nick
    name or adding a last name to distinguish between similarly named Employees.

    :param new_name: An updated version of the Employee's name. 
    :param type: string
    """
    self.name = new_name

  def set_max_shifts(self, max_shifts: int):
    """
    Sets or updates an Employee's maximum number of shifts they wish to work per week, while also calculating their 
    scheduling priority.

    :param max_shifts: The maximum number of shifts to work each week.
    :param type: integer
    """
    self.max_shifts = max_shifts
    days_available = 0
    for k, v in self.availability.items():
      for hour in v:
        if hour == 1:
          days_available += 1
          break
        else:
          continue
    self.priority = round((max_shifts / days_available), 3)

  def set_split_shifts(self, updated_setting: bool):
    """
    Updates an Employee's willingness to work split shifts. True is willing, False is unwilling.

    :param updated_setting: The status of the Employee's willingness.
    :param type: boolean
    """
    self.splits = updated_setting

  def change_availability(self, new_availability):
    """
    Update's an Employee's availability using a CSV file.

    :param new_availability: CSV file containing an Employee's updated availability.
    :param type: TBD
    """
    self.availability = new_availability
  
  def show_info(self):
    """
    Display basic Employee information in a user-friendly format.
    """
    print("Name:", self.name)
    print("Accepts Split-Shifts:", self.splits)
    print("Max Shifts per Week:", self.max_shifts)
    print("Scheduling Priority:", self.priority)

  def parse_availability(self):
    """
    Displays the Employee's availability in a user-friendly format.
    """
    for day, timeblocks in self.availability.items():
      print("Availability for", self.name, "on:")
      print(day)
      for timeslot, available in zip(timeblocks, self.times):
        if timeslot == 1:
          print(available)
