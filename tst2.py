import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# === Bahnparameter ===
r = 1
theta = np.linspace(0, np.pi, 300)  # für halbe Zykloide
x_brach = r * (theta - np.sin(theta))
y_brach = r * (1 - np.cos(theta))

x_line = np.linspace(0, x_brach[-1], 300)
y_line = np.linspace(0, y_brach[-1], 300)

# === Kugelbewegung ===
frames = 100
t_vals = np.linspace(0, np.pi, frames)
x_b = r * (t_vals - np.sin(t_vals))
y_b = r * (1 - np.cos(t_vals))

x_l = np.linspace(0, x_b[-1], frames)
y_l = np.linspace(0, y_b[-1], frames)

# === Ploterstellung ===
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_brach, y_brach, label="Brachistochrone", linewidth=2)
ax.plot(x_line, y_line, '--', label="Gerade Bahn", linewidth=2)

ball_b, = ax.plot([], [], 'o', color='blue', markersize=10, label="Kugel (Zykloide)")
ball_l, = ax.plot([], [], 'o', color='red', markersize=10, label="Kugel (Gerade)")

ax.set_xlim(0, x_brach[-1])
ax.set_ylim(y_brach[-1]-0.1, 0.1)
ax.invert_yaxis()
ax.set_title("Murmelrennen: Wer ist schneller?")
ax.set_xlabel("Horizontaler Abstand")
ax.set_ylabel("Höhe")
ax.axis("equal")
ax.grid(True)
ax.legend()


def update(frame):
    ball_b.set_data([x_b[frame]], [y_b[frame]])
    ball_l.set_data([x_l[frame]], [y_l[frame]])
    return ball_b, ball_l


ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# === Video speichern (optional) ===
ani.save("brachistochrone_animation.mp4", writer="ffmpeg", fps=30)
print("Animation gespeichert als 'brachistochrone_animation.mp4'")
