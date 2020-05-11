'''

Using sigmoid for activation fcn: https://en.wikipedia.org/wiki/Sigmoid_function
    
    S(x) = 1 / ( 1 + e⁻ˣ )

    Imagine they're all connected :)
    This will be a fully connected network

Four input nodes          Three hidden nodes       One output node

○ ------╦---------------------> ○ ----------------╗                                      
i1      |                       h1                |      
        |                                         |
        |                                         |
        |                                         |
○       |                                         |
i2      |                                         |
        |                                         |
        ╚---------------╦-----> ○ ----------------╬---> ○
                        |       h2                |     o1
○                       |                         |
i3                      |                         |
                        |                         |
                        |                         |
○                       ╚-----> ○ ----------------╝
i4                              h3


Hidden = S(Weighted Sums * Input + Bias)
        
    Weight Sums is from input to hidden
    Bias is hidden's bias
        
    Hᵢ = S(Wᵢⱼ * Iᵢ + Bᵢ)
        
Output = S(Weighted Sums * Hidden + Bias)
    
    Weight Sums is from hidden to output
    Bias is output's bias
       
    Oᵢ = S(Wᵢⱼ * Hᵢ + Bᵢ)

'''

import math
import numpy as np

def sigmoid_fcn(x):
    return 1 / (1 + math.exp(-x))

class NeuralNet:
    def __init__(self, inputN, hiddenN, outputN, lr):
        self.nodes_input = inputN
        self.nodes_hidden = hiddenN
        self.nodes_output = outputN

        self.learning_rate = lr

        # weights
        self.w_ih = np.random.normal(0.0, pow(self.nodes_hidden, -0.5), (self.nodes_hidden, self.nodes_input))
        self.w_ho = np.random.normal(0.0, pow(self.nodes_output, -0.5), (self.nodes_output, self.nodes_hidden))

        # bias
        self.bias_h = np.random.rand(self.nodes_hidden, 1)
        self.bias_o = np.random.rand(self.nodes_output, 1)

    def test(self, user_input):
        inputs = np.array(user_input, ndmin=2).T

        print(inputs, self.w_ih)
        hidden_ins = np.dot(self.w_ih,inputs)
        hidden_ins = np.add(hidden_ins, self.bias_h)
        hidden_outs =  hidden_ins * sigmoid_fcn(hidden_ins)
        
        output_ins = np.dot(self.w_ho, hidden_outs)
        output_ins = np.add(output_ins, self.bias_o)
        output_outs = output_ins * sigmoid_fcn(output_ins)
        
        return np.array(output_outs)
    
    def train(self, user_input, user_goal):
        inputs = np.array(user_input, ndmin=2).T
        goal = np.array(user_goal, ndmin=2).T

        hidden_ins = np.dot(self.w_ih,inputs)
        activate_hidden = sigmoid_fcn(hidden_ins)
        hidden_outs =  hidden_ins * activate_hidden

        output_ins = np.dot(self.w_ho, hidden_outs)
        activate_output = sigmoid_fcn(output_ins)
        output_outs = output_ins * activate_output

        output_err = goal - output_outs
        hidden_err = np.dot(self.w_ho.T, output_err)

        self.w_ho += self.learning_rate * np.dot((output_err * output_outs * (1 - output_outs)), hidden_outs.T)
        
        self.w_ih += self.learning_rate * np.dot((hidden_err * hidden_outs * (1 - hidden_outs)), inputs.T)
        
        pass
