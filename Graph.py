import matplotlib.pyplot as plt
import numpy as np

# Generate x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 1000)

# Compute sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='Sine', color='blue')
plt.plot(x, y_cos, label='Cosine', color='red')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()

# Add grid
plt.grid(True)

# Show the plot
plt.show()
