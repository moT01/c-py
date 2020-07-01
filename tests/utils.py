# get last line from .cwd file
def getCwd():
  f=open("./tests/.cwd", "r")
  if f.mode == 'r':
      contents =f.readlines()
      return contents[-1].strip()

# get last line from .bash_history
def getLastCommand():
  f=open("../.bash_history", "r")
  if f.mode == 'r':
      contents =f.readlines()
      return contents[-1].strip()