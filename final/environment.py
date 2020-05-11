from perceptron import Perceptron
from shape import Shape, label_to_shape
import random
from consoleColors import bcolors
from neuralnet import NeuralNet
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from points import Point
'''
p = Perceptron()

shapes = []

for i in range(10000):
    shapes.append(Shape(random.uniform(-1,1), random.uniform(-1,1)))

total = 0
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

print('Perceptron Accuracy with colors: {:.1%}'.format(correct/total))

'''

neural_net = NeuralNet(2,3,1, 0.3)

epoch = 12
sample_size = 100

points = []

for i in range(sample_size):
    points.append(Point())

x = np.arange(0, 4*np.pi,0.1)
y = np.sin(x) 
fig, ax = plt.subplots()
ax.plot(x,y)

for i in range(sample_size):
    guess = neural_net.test([points[i].get_x(),points[i].get_y()])
    if (guess > 0.5):
        ax.plot(points[i].get_x(), points[i].get_y(), 'go') # should be above curve
    else:
        ax.plot(points[i].get_x(), points[i].get_y(), 'ro') # should be below curve

plt.title('ML test w/o training')

incorrect_guess = mpatches.Patch(color='red', label='incorrect')
correct_guess = mpatches.Patch(color='green', label='correct')
plt.legend(handles=[incorrect_guess, correct_guess])

x = np.arange(0, 4*np.pi,0.1)
y = np.sin(x) 
fig, ax = plt.subplots()
ax.plot(x,y)

for i in range(epoch):
    for j in range(len(points)):
        neural_net.train([points[j].get_x(),points[j].get_y()], [points[j].get_label()])

for i in range(sample_size):
    guess = neural_net.test([points[i].get_x(),points[i].get_y()])
    if (guess == 1):
        ax.plot(points[i].get_x(), points[i].get_y(), 'go') # trained, above
    else:
        ax.plot(points[i].get_x(), points[i].get_y(), 'ro') # trained, below

plt.title('ML test w/ training')

incorrect_guess = mpatches.Patch(color='red', label='incorrect')
correct_guess = mpatches.Patch(color='green', label='correct')
plt.legend(handles=[incorrect_guess, correct_guess])

plt.show()