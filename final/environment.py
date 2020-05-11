from perceptron import Perceptron
from shape import Shape, label_to_shape
import random
from consoleColors import bcolors
from neuralnet import NeuralNet

p = Perceptron()

shapes = []

for i in range(10000):
    shapes.append(Shape(random.uniform(-1,1), random.uniform(-1,1)))

'''total = 0
correct = 0

for i in range(len(shapes)):
    total = total + 1
    inputs = [shapes[i].get_shape_type(), shapes[i].get_shape_color()]
    goal = shapes[i].get_shape_label()
    p.train(inputs, goal)

    guess = p.guess(inputs)

    if (guess == goal):
        correct = correct + 1
        print('====================\n' + bcolors.OKGREEN + f'Guess: {label_to_shape(guess)} \nActual: {label_to_shape(goal)}' + bcolors.ENDC)
    else:
        print('====================\n' + bcolors.FAIL + f'Guess: {label_to_shape(guess)} \nActual: {label_to_shape(goal)}' + bcolors.ENDC)

print('Perceptron Accuracy with 1 layer (colors): {:.1%}'.format(correct/total))

'''

neural_net = NeuralNet(2,1,1, 0.1)
