class Point:
    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, other):
        print('add called')
        return Point(self.value + other.value)
    
    def __sub__(self, other):
        print('add called')
        return Point(self.value - other.value)
    
p1 = Point(10)
p2 = Point(20)
p3 = p1+p2
print(p3.value)
p3 = p2-p1
print(p3.value)
