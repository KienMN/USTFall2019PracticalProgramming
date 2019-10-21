# Test encapsulation of classes.
# We are not able to change private attribute of the class from outside scope of the class.
# Author: Kien Mai Ngoc

from shapes import Circle

if __name__ == "__main__":
  print('Test encapsulation:')
  
  # Initializing object.
  circle = Circle(radius=4)

  # Getting info of the original object.
  print('Original circle object.')
  print(circle.get_info())

  # Changing value of private attribute directly.
  circle.__radius = 5
  print('The circle object after changing the radius directly.')
  print(circle.get_info())

  # Changing value of private attribute via class method.
  circle.change_radius(new_radius=5)
  print('The circle object after using change_radius method.')
  print(circle.get_info())