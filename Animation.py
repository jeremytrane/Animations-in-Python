import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(10, 10))  # Set a square figure 10x10 inches
line, = ax.plot([], [], color='white', linewidth=0.5)  # Set line color to white and line width to 0.5

ax.set_facecolor('black') # Set background color to black
ax.set_aspect('equal')  # Equal aspect ratio
ax.grid(False)  # Turn off the grids
ax.set_xlim(-2.5, 2.5) # X-axis limit
ax.set_ylim(-2.5, 2.5) # Y-axis limit

theta_degrees = np.linspace(0, 113*360, 10000)
theta_radians = np.deg2rad(theta_degrees)

def animate(i):
    z = np.exp(theta_radians[:i] * 1j) + np.exp(np.pi * theta_radians[:i] * 1j)
    x = np.real(z)
    y = np.imag(z)
    line.set_data(x, y)
    return line,

# Number of frames = number of points in theta_degrees
num_frames = len(theta_degrees)

# Calculate the interval to achieve 15 seconds of animation
total_time_ms = 15000  # 15 seconds in milliseconds
interval = total_time_ms / num_frames

ani = FuncAnimation(fig, animate, frames=num_frames, interval=interval, blit=True)

plt.show()
