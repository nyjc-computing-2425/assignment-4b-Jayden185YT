stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below

#validating the E notation
valid = True
good_char = "012345678910Ex.-^"
for char in stdform:
  if char not in good_char:
    valid = False
    break

period = False
multiply = False
caret = False
for char in stdform:
  if char == '.' and period:
    valid = False
    break
  if char == 'x' and multiply:
    valid = False
    break
  if char == '^' and caret:
    valid = False
    break

  if char == '.':
    period = True
  elif char == '-':
    hyphen = True
  elif char == '^':
    caret = True

pos_pow = stdform.index('^')
if stdform[pos_pow+1] == '-':
  if not stdform[pos_pow+2:].isdigit():
    valid = False
else:
  if not stdform[pos_pow+1:].isdigit():
    valid = False
    
#printing the E notation
if valid:
  pos_x = stdform.index('x')
  eform = ""
  eform = eform + stdform[:pos_x] + 'E'
  eform = eform + stdform[pos_x+3 : pos_pow]
  eform = eform + stdform[pos_pow+1:]
  print("This number in E notation is", eform + ".")
else:
  print("Error converting to scientific E notation.")