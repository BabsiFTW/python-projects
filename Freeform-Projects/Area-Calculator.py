"""Calculator, that can compute the area of the following shapes:
- Circle
- Triangle
"""
print("Hello, what should I calculate?")
option = raw_input("Enter C for circle or T for Triangle: ")

if option.upper() == "C":
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius**2
  print("The result is " + str(area))
  
elif option.upper() == "T":
  base = float(raw_input("Enter base length: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print("The result is " + str(area))
  
else:
  print("Please enter C for circle or T for triangle!")
  
print("See you soon!")
