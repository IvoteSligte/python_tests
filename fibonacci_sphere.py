from math import atan2
from operator import mod
import mpl_toolkits.mplot3d.axes3d as ax3d
import numpy as np


# credit goes to: https://gist.github.com/Seanmatthews/a51ac697db1a4f58a6bca7996d75f68c
def fibonacci_sphere(num_points: int) -> np.ndarray:
    ga = (3 - np.sqrt(5)) * np.pi # golden angle                                                                             

    # Create a list of golden angle increments along tha range of number of points                                           
    theta = ga * np.arange(num_points)

    # Z is a split into a range of -1 to 1 in order to create a unit circle                                                  
    z = np.linspace(1/num_points-1, 1-1/num_points, num_points)

    # a list of the radii at each height step of the unit circle                                                             
    radius = np.sqrt(1 - z * z)

    # Determine where xy fall on the sphere, given the azimuthal and polar angles                                            
    y = radius * np.sin(theta)
    x = radius * np.cos(theta)
    
    return np.array(list(zip(x, y, z)))

def inverse_fibonacci_sphere(num_points: int, vector: np.ndarray) -> float:
    if vector.shape != (3,):
        raise ValueError(f"Incorrect vector shape, must be (None, 3), is: {vector.shape}")
    
    ga = (3 - np.sqrt(5)) * np.pi # golden angle
    
    z = vector[2]
    
    theta = atan2(vector[1], vector[0])
    
    z_index = num_points - 1 - ((num_points - 1) / 2.0) * (z / (1.0 / num_points - 1.0) + 1.0)
    
    z_theta = mod(ga * z_index, 2.0 * np.pi)
    
    deviation = mod((theta - z_theta) / (2.0 * np.pi) + 0.5, 1.0) - 0.5
    
    circles = (ga * num_points) / (2.0 * np.pi)
    
    indices_circle = num_points / circles
    
    index_offset = deviation * indices_circle
    
    return z_index + index_offset

if __name__ == '__main__':
    num_points = int(input("number of points: "))
    points = fibonacci_sphere(num_points).tolist()
    print(points)
    
    import xerox
    import json
    # import random
    # random.shuffle(points)
    xerox.copy(json.dumps(points))
    
    print("Copied to clipboard.")
