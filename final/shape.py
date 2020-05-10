'''

    I am going to define arbitrary values that our perceptron will use to classify colors

    A shape that has color blue, and type of square will have label == 1
    A shape that has color red, and type of square will have label == 1

'''

def label_to_shape(label):
    if (label == 1):
        return 'Blue Square'
    elif (label == -1):
        return 'Red Square'
    else:
        return 'ERROR'

class Shape:
    def __init__(self, shapeType, color):
        self.shape_type = shapeType
        self.shape_color = color
        
        if (self.shape_color <= 0.5 and self.shape_type <= 0.5):
            self.shape_label = 1 # 'Blue Square'
        else:
            self.shape_label = -1 # 'Red Square'

    def whatAmI(self):
        print(f'I am a {self.shape_type}! My color is: {self.shape_color}')

    def get_shape_type(self):
        return self.shape_type

    def get_shape_color(self):
        return self.shape_color

    def get_shape_label(self):
        return self.shape_label