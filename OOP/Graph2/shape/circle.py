# 載入math模組，我們要使用它的pi值
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def show_shape_info(self):
        print('圓形，半徑' + str(self.__radius))

    def get_area(self):
        return math.pi * self.__radius * self.__radius
