from Rectangle import Rectangle,Square,Circle

#creating two rectangles

rect1 = Rectangle(3,4)
rect2 = Rectangle(12,5)

#get areas of our rectangles

print("Rectangle 1 area is",rect1.get_area())
print("Rectangle 2 area is",rect2.get_area())
print("- - - - -")

square1 = Square(5)
square2 = Square(10)

print("Square 1 area is",square1.get_area_square())
print("Square 2 area is",square2.get_area_square())
print("- - - - -")

circle1 = Circle(4)
circle2 = Circle(6)

print("Circle 1 area is", circle1.get_area_circle())
print("Circle 2 area is", circle2.get_area_circle())
print("- - - - -")

figures = [rect1, rect2, square1, square2, circle1, circle2]
for figure in figures:
    if isinstance(figure, Square):
        print("Square area is",figure.get_area_square())
    elif isinstance(figure, Circle):
        print("Circle area is",figure.get_area_circle())
    else:
        print("Rectangle area is",figure.get_area())