# Imports erneut laden nach Code-Reset
import numpy as np
import matplotlib.pyplot as plt

# Parameter für die Zykloide (Brachistochrone)
r = 1  # Radius der Kreisbahn, der die Zykloide erzeugt
theta = np.linspace(0, np.pi, 300)  # Winkelbereich für halbe Zykloide

# Zykloide berechnen (parametrische Form)
x_brach = r * (theta - np.sin(theta))
y_brach = r * (1 - np.cos(theta))

# Gerade Bahn
x_line = np.linspace(0, x_brach[-1], 300)
y_line = np.linspace(0, y_brach[-1], 300)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x_brach, y_brach, label="Brachistochrone (Zykloide)", linewidth=3)
plt.plot(x_line, y_line, '--', label="Gerade Bahn", linewidth=2)
plt.gca().invert_yaxis()  # Damit unten auch unten ist
plt.title("Welche Kugel ist schneller?")
plt.xlabel("Horizontaler Abstand")
plt.ylabel("Höhe")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
