import random

def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

class Perceptron:
    def __init__(self):
        self.learning_rate = 0.1
        self.weights = [None] * 2
        self.weights = [random.uniform(-1,1) for w in self.weights]
    
    def guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        return sign(sum)

    # tuning weights w/ supervised learning
    def train(self, inputs, goal):
        guessing = self.guess(inputs)
        error = goal - guessing
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learning_rate