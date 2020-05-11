import random
import math

def label_to_type(label):
    if (label >= 1):
        print('above')
    else:
        print('below')

class Point:
    def __init__(self):
        self.x = random.uniform(0,12)
        self.y = random.uniform(-1,1)

        if (self.y > math.sin(self.x)):
            self.label = 1 # above sin curve
        else:
            self.label = -1 # below sin curve

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_label(self):
        return self.label