from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
from scipy import integrate
fig = plt.figure()
style.use('ggplot')
ax = fig.add_subplot(2, 1, 1, projection = '3d') # 3d graph projection
#=================First Subplot==============#
#Calculate volume under the 2D curve, generating impulse or work depending on the context of the problem

plt.title("Graph Of A Multi-Variable Function\nf(x, y)\nLook at the console for more details")
def f(x, y):
    return np.sin(x**2)+np.sin(y**2)
    
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X,Y) #defines the value of Z as the output of the function f
ax.contour3D(X,Y,Z, 50, cmap='viridis') # purple is the lowest point, bright green is highest point
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(30, 60)   #change the angle you view at
fig.show()
g = lambda x, y: np.sin(x**2) + np.sin(y**2)
i, j = integrate.dblquad(g, 0, 2, lambda y: 0, lambda y: 2)
print("This is a multi-variable function represent by the equation sin(x^2)+sin(y^2)")
print("The volume of this function in the given bounds is",i, "units cubed. This function models real life situations that happen periodically, and knowing the area under the curve, helps scientists figure out meaningful statistics such as impulse (the area/volume under the curve) ")#gives you area 
print("You could even find out the mass of this 2D object by using a density function, but it'll be easier on a more simplistic 2D object")
#===========Second Subplot======================#
#========Calculate Mass or Combined Electric Charge======#

ax = fig.add_subplot(2, 1, 2, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Finding the mass\nof a lamina (2D Shape) using physics")
plt.legend()
x = [0, 0, 1, 0] 
y = [0, 1, 0, 0]
x1 = [0, 0 ]  #connections to the bottom axes to show what a prism of the shape would look like
y1 = [0, 0]   #easier to visualize the volume, density and mass
z1 = [-0.06, 0]
x2 = [1, 1]
y2 = [0, 0]
z2 = [-0.06, 0]
x3 = [0, 0]
y3 = [1, 1]
z3 = [-0.06, 0]

# plot a 3D wireframe 
plt.plot(x, y, label = "Original Lamina Shape") 
plt.plot(x1, y1, z1, label = "Connection")
plt.plot(x2, y2, z2, label = "Connection1")
plt.plot(x3, y3, z3, label = "Connection2")
plt.legend() # initialize the legend
plt.show() #show the legend on the subplot
def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    text.set_position((xdata[ind], ydata[ind]))
    text.set_text(zip(xdata[ind], ydata[ind]))
fig.canvas.mpl_connect('pick_event', onpick)
one_var = lambda x: ((1-x)**2)/2
mass_lamina, e = integrate.quad(one_var, 0, 1)
print("The mass of this lamina, given the density function of p(x, y) = d, is", mass_lamina, "units. To find this, you need to look at the coordinates of the lamina, then take the integral of the function taking into consideration the domain.")
print("Also, you could think of this as the combined electric charge of the lamina, and the density function could be the charge distribution")
print("This is because the mathematical relationship between gravity and electricity is strikingly similar (Couloumb's Law and Newton's Universal Law of Gravitation are strikingly similar)")
fig.show()
plt.show()

#This simulation and graph can tell physicists a lot about charge distribution of a certain function, or give them an idea of where the center of mass is potentially located
#These type of distribution can be used in statistics as well
