from abc import abstractmethod, ABC


class Shape(ABC):

    def __init__(self, name: str) -> None:
        self._name = name

    @abstractmethod
    def __str__(self) -> str:
        pass


class Dot(Shape):

    def __init__(self, name: str, x: float, y: float, z: float):
        super().__init__(name)
        self._x = x
        self._y = y
        self._z = z

    def __str__(self) -> str:
        return f"It's a dot named: {self._name}. "

    def get_figure_center(self):
        print(f"x: {self._x}, y: {self._y}, z: {self._z}.")


class Segment(Dot):

    def __init__(self, name: str, x: float, y: float, z: float, end_x: float, end_y: float, end_z: float):
        super().__init__(name, x, y, z)
        self._end_x = end_x
        self._end_y = end_y
        self._end_z = end_z

    def __str__(self) -> str:
        return f"It's a segment named: {self._name}. "

    def get_figure_center(self):
        center_x = self._x + self._end_x / 2
        center_y = self._y + self._end_y / 2
        center_z = self._z + self._end_z / 2
        print(f"x: {center_x}, y: {center_y}, z: {center_z}.")


class Circle(Dot):

    def __init__(self, name: str, x: float, y: float, z: float, radius: float):
        super().__init__(name, x, y, z)
        self._radius = radius

    def __str__(self) -> str:
        return f"It's a circle named: {self._name}. Radius: {self._radius}."


class Rectangle(Dot):

    def __init__(self, name: str, x: float, y: float, z: float, height: float, length: float):
        super().__init__(name, x, y, z)
        self._height = height
        self._length = length

    def __str__(self) -> str:
        return f"It's a rectangle named: {self._name}. Height: {self._height}, length: {self._length}."


class Parallelepiped(Rectangle):

    def __init__(self, name: str, x: float, y: float, z: float, height: float, length: float, width: float):
        super().__init__(name, x, y, z, height, length)
        self._width = width

    def __str__(self) -> str:
        return f"It's a parallelepiped named: {self._name}. Height: {self._height}, length: {self._length}, width: {self._width}."
