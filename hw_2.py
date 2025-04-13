class Figure:
    unit = "cm"
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print (f"Square side length: {self.__side_length} {self.unit},"
                f" area: {self.calculate_area()} {self.unit} ")

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f"Rectangle length: {self.__length}{self.unit},"
              f"width: {self.__width}{self.unit},"
              f" area: {self.calculate_area()}{self.unit}")

sq_1 = Square(6)
sq_2 = Square(3)
rec_1 = Rectangle(4, 7)
rec_2 = Rectangle(2, 6)
rec_3 = Rectangle(3, 5)
figures_list = [sq_1, sq_2, rec_1, rec_2, rec_3]
for figure in figures_list:
    print(figure.info())