from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# <Example 1> 3D points and lines
ax = plt.axes(projection='3d')
# Data for a 3D line
zline = np.linspace(0, 15, 100)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'blue')

#Data for 3D scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
plt.show(block=False)
plt.pause(3)
plt.close()

# <Example 2> 3D contour plots
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2 ))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
# meshgrid returns coordinate matrices from coordinate vectors
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# Tilting the view from above
ax.view_init(60, 25)
plt.show(block=False)
plt.pause(3)
plt.close()

# <Example 3> wireframes
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='blue')
ax.set_title('wireframe')
plt.show(block=False)
plt.pause(3)
plt.close()

# <Example 4> Surface Plots
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_title('surface plot')
plt.show(block=False)
plt.pause(3)
plt.close()

# <Example 5> Cont'd
r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
r, theta = np.meshgrid(r, theta)
X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none');
plt.show(block=False)
plt.pause(3)
plt.close()

# <Example 6>
theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5);
plt.show(block=False)
plt.pause(3)
plt.close()

# or
ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none');
plt.show(block=False)
plt.pause(3)
plt.close()

