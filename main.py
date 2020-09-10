# Author: August Sanderson aes6218@psu.edu
# Collaborator: Dymea Schippers dxs5940@psu.edu
# Collaborator: Jonathan Ahn jxa5570@psu.edu
# Collaborator: Ronit Ramnarayan rvr5507@psu.edu
# Collaborator: Nicholas Glaz nsg5204@psu.edu
# Section: 11
# Breakout: 2

def getLetterGrade(grade):
  if grade >= 93.0:
    return "A"
  elif grade >= 90.0:
    return "A-"
  elif grade >= 87.0:
    return "B+"
  elif grade >= 83.0:
    return "B"
  elif grade >= 80.0:
    return "B-"
  elif grade >= 77.0:
    return "C+"
  elif grade >= 70.0:
    return "C"
  elif grade >= 60.0:
    return "D"
  else:
    return "F"

def run():
  number = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(number)}.")

if __name__ == "__main__":
  run()