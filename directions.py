from math import cos, pi, sin
import matplotlib.pyplot as plt

vectors = []

for x in range(8):
    x = (x / 8.0) * 2.0 * pi
    
    for y in range(8):
        y += 0.5
        y = (y / 8.0) * pi - pi / 2.0
        
        vectors.append([sin(x) * cos(y), cos(x) * cos(y), sin(y)])

print(vectors)

X, Y, Z = zip(*vectors)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X, Y, Z)

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
plt.show()