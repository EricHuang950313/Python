class ShapeObject:
    def show_shape_info(self):
        raise NotImplementedError(
            '子類別必須覆寫show_shape_info()方法')

    def get_area(self):
        raise NotImplementedError(
            '子類別必須覆寫get_area()方法')
