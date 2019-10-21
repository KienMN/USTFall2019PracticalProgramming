# Shape base class.
# Author: Kien Mai Ngoc

from abc import ABC, abstractmethod
# ABC stand for Abstract based classes

class Shape(ABC):
  """Base class for shapes."""

  @abstractmethod
  def __init__(self):
    """Initialize a shape instance."""
    raise NotImplementedError

  @abstractmethod
  def get_info(self):
    """Getting information about the shape."""
    raise NotImplementedError

  @abstractmethod
  def calculate_surface(self):
    """Computing the surface of the shape."""
    raise NotImplementedError

  @abstractmethod
  def calculate_perimeter(self):
    """Computing the perimeter of the shape."""
    raise NotImplementedError