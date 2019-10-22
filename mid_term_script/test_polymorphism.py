# Test polymorphism of classes.
# The same methods will be handled differently depending on different classes.
# Author: Kien Mai Ngoc.

from shapes import Circle, Square

if __name__ == "__main__":
  print('Test Polymorphism:')

  # Initializing objects
  circle = Circle(radius=3)
  square = Square(side=3)

  # Calling methods
  print('1. Info:')
  print(circle.get_info())
  print(square.get_info())

  print('2. Calculating surface:')
  print('Circle:', circle.calculate_surface())
  print('Square:', square.calculate_surface())

  print('3. Calculating perimeter:')
  print('Circle:', circle.calculate_perimeter())
  print('Square:', square.calculate_perimeter())