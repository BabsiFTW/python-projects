"""
    1. Prompt the user for the type of conversion they want
    2. Ask the user to input the RGB or Hex value
    3. Use Bitwise operators and shifting in order to convert the value
    4. Print the converted value to the user
"""
def rgb_hex():
  invalid_msg = "Invalid values were entered!"
  red = int(raw_input("Please enter the red value: "))
  if red < 0 or red > 255:
    print invalid_msg
    return
  green = int(raw_input("Please enter the green value: "))
  if green < 0 or green > 255:
    print invalid_msg
    return
  blue = int(raw_input("Please enter the blue value: "))
  if blue < 0 or blue > 255:
    print invalid_msg
    return
  val = (red << 16) + (green << 8 ) + blue
  #converting the RGB value to a hex value
  print "%s" % (hex(val)[2:]).upper()

def hex_rgb():
  hex_val = raw_input("Please enter the hexadecimal value: ")
  if len(hex_val) != 6:
    print "Invalid Value was entered!"
    return
  else:
    #16: indicates that hex_val is in base 16
    hex_val = int(hex_val, 16)
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "Red: %s Green: %s Blue: %s" % (red, green, blue)
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print "RGB tp Hex ..."
      rgb_hex()
    elif option == "2":
      print "Hex to RGB ..."
      hex_rgb()
    elif option == "X" or option == "x":
      break
    else:
      print "Error! Invalid user input!"
convert()
