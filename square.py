class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """
        pass
    
    def area(self) -> float:
        """
        This method finds the area of the square.
        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        return self.square_side**2

    def perimeter(self) -> float:
        """
        This method finds the perimeter of the square.
        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        return 4*self.square_side
a=Square(2)
print(a.is_valid())
print(a.area())
print(a.perimeter())

