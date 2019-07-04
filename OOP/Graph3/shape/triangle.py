from shape.shapeobject import *

class Triangle(ShapeObject):
    def __init__(self, bottom, height):
        self.__bottom = bottom
        self.__height = height

    def show_shape_info(self):
        print('三角形，底' + str(self.__bottom) + '，'
              + '高' + str(self.__height))

    def get_area(self):
        return self.__bottom * self.__height / 2
