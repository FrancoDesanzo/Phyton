# Write code below 💖
import math

#Drawing the MENU
f = 1 # "F" for flag, to control the while loop
while (f != 0):
  print("-----------------------------")
  print("📏 Area Calculator - MENU 📏")
  print("-----------------------------")
  print("1- Square 🟪")
  print("2- Rectangle ⌨️")
  print("3- Triangle 🔺")
  print("4- Circle 🟢")
  print("")
  print("0- EXIT")
  print("---------------------")
  
  #Input of the option
  f = int(input("Select an option (0 to exit): ")) 

  #Square Area
  if (f == 1):
    print("")
    print("-------------------")
    print(" #Square Area 🟪")
    print("-------------------")
    squeare_s = int(input("Long of one side: "))
    squeare_area = squeare_s ** 2
    print("")
    print("The area of the SQUARE is: " + str(squeare_area))
    print("")
  
  #Rectangle Area
  elif (f == 2):
    print("")
    print("-------------------")
    print(" #Rectangle Area ⌨️")
    print("-------------------")
    rectangle_l = int(input("Lenght: ")) #Input of the Lenght
    rectangle_w = int(input("Width: ")) #Input of the Width
    rectangle_area = rectangle_l * rectangle_w
    print("")
    print("The area of the RECTANGLE is: " + str(rectangle_area))
    print("")

  #Triangle Area
  elif (f == 3):
    print("")
    print("-------------------")
    print(" #Triangle Area 🔺")
    print("-------------------")
    triangle_h = int(input("Height: ")) #Input of the Height
    triangle_b = int(input("Base: ")) #Input of the Base
    triangle_area = (triangle_h * triangle_b)/2
    print("")
    print("The area of the TRIANGLE is: " + str(triangle_area))
    print("")

  #Circle Area
  elif (f == 4):
    print("")
    print("-----------------")
    print(" #Circle Area 🟢")
    print("-----------------")
    circle_r = int(input("Radius: ")) #Input of the Height
    circle_area = (circle_r ** 2) * math.pi
    print("")
    print("The area of the CIRCLE is: " + str(circle_area))
    print("")

  #EXIT
  elif (f == 0):
    print("")
    print("-----------------------------------")
    print("Bye 👋,thanks for using my program")
    print("-----------------------------------")

  else:
    print("")
    print("Please select an available option (1/2/3/4 / 0)")
    print("")
