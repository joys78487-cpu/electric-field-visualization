import numpy as np
import matplotlib.pyplot as plt

# Coulomb constant
k = 8.99e9

# Create grid
x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)
X, Y = np.meshgrid(x, y)

# Define charges: (q, x0, y0)
charges = [
    (1e-9, -1, 0),   # Positive charge
    (-1e-9, 1, 0)    # Negative charge
]

# Initialize electric field components
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)

# Compute field
for q, x0, y0 in charges:
    dx = X - x0
    dy = Y - y0
    r = np.sqrt(dx**2 + dy**2) + 1e-9
    
    Ex += k * q * dx / r**3
    Ey += k * q * dy / r**3

# Plot field lines
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, Ex, Ey, density=1.5)

# Plot charges
for q, x0, y0 in charges:
    if q > 0:
        plt.scatter(x0, y0, color='red', s=100)
    else:
        plt.scatter(x0, y0, color='blue', s=100)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Electric Field Visualization")
plt.grid()
plt.savefig("electric_field.png")
plt.show()
