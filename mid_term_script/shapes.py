# Shapes classes inherit from shape base class.
# Author: Kien Mai Ngoc

from shape_base import Shape
import math

class Circle(Shape):
  """The circle shape.

  Parameters
  ----------
  radius : float
    The radius of the circle shape.

  Attributes
  ----------
  __radius : float
    The radius of the circle shape.
  """

  def __init__(self, radius):
    # Private attribute
    self.__radius = radius

  def get_info(self):
    """Getting information about the shape.

    Returns
    -------
    s : str
      The information about the shape.
    """
    return "Circle shape with radius of {}".format(self.__radius)

  def calculate_surface(self):
    """Computing the surface of the circle shape.

    Returns
    -------
    surface : float
      The value of the surface of the circle shape.
    """
    surface = math.pi * self.__radius ** 2
    return surface

  def calculate_perimeter(self):
    """Computing the perimeter of the circle shape.

    Returns
    -------
    perimeter : float
      The value of the perimeter of the circle shape.
    """
    perimeter = 2 * math.pi * self.__radius
    return perimeter

  def change_radius(self, new_radius):
    """Changing the radius of the circle shape instance.
    
    Parameters
    ----------
    new_radius : float
      The new value of the radius.

    Returns
    -------
    self : object
      The instance itself.
    """
    self.__radius = new_radius
    return self

class Square(Shape):
  """The square shape.

  Parameters
  ----------
  side : float
    The value of the side of the square shape.

  Attributes
  ----------
  __side : float
    The value of the side of the square shape.
  """

  def __init__(self, side):
    # Private attribute
    self.__side = side

  def get_info(self):
    """Getting information about the shape.

    Returns
    -------
    s : str
      The information about the shape.
    """
    return "Square shape with side of {}".format(self.__side)

  def calculate_surface(self):
    """Computing the surface of the square shape.

    Returns
    -------
    surface : float
      The value of the surface of the square shape.
    """
    surface = self.__side ** 2
    return surface

  def calculate_perimeter(self):
    """Computing the perimeter of the square shape.

    Returns
    -------
    perimeter : float
      The value of the perimeter of the square shape.
    """
    perimeter = self.__side * 4
    return perimeter

  def change_side(self, new_side):
    """Changing the side of the square shape instance.
    
    Parameters
    ----------
    new_side : float
      The new value of the side.

    Returns
    -------
    self : object
      The instance itself.
    """
    self.__side = new_side
    return self