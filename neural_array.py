import matplotlib.pyplot as plt
import random

data = [1, 2, 3, 4, 5, 6, 7, 8]

num_nodes = 4
training_factor = 0.001
iterations = 100
weight_range = 1.0
bias_range = 1.0

weights = [(random.random() * 2.0 - 1.0) * weight_range for _ in range(num_nodes)]
biases = [(random.random() * 2.0 - 1.0) * bias_range for _ in range(num_nodes)]

def predict_layer(input: int):
    global weights
    
    return [w * input + b for w, b in zip(weights, biases)]

def predict(input: int):
    return sum(predict_layer(input))


def backpropagate(input: int, desired_output: float):
    global weights
    
    values = predict_layer(input)
    output = sum(values)
    for j, v in enumerate(values):
        diff = desired_output - (output - v)
        
        ideal_weight = 0
        if input != 0:
            ideal_weight = diff / input
        weights[j] += (ideal_weight - weights[j]) * training_factor
        
        ideal_bias = diff
        biases[j] += (ideal_bias - biases[j]) * training_factor


def train():
    global data
    
    for input, desired_output in enumerate(data):
        backpropagate(input, desired_output)

for _ in range(iterations):
    train()

desired_results = data
results = [predict(input) for input in range(len(data))]

print(results)

plt.plot(range(len(data)), desired_results, label="desired_results")
plt.plot(range(len(data)), results, label="results")
plt.legend()
plt.show()
