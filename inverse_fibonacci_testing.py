from fibonacci_sphere import fibonacci_sphere, inverse_fibonacci_sphere

num_points = 64
points = fibonacci_sphere(num_points)

dev = 0

for i, p in enumerate(points):
    idx = inverse_fibonacci_sphere(num_points, p)
    dev += abs(i - idx)
    print(i, idx)
    
print("deviation", dev)

