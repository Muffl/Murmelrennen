import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# === Bahnparameter ===
r = 1
theta = np.linspace(0, np.pi, 300)

# Zykloide (Brachistochrone) korrekt orientiert (nach unten)
x_brach = r * (theta - np.sin(theta))
y_brach = r * (1 - np.cos(theta))  # positiv

# Gerade Bahn vom Start- zum Endpunkt
x_line = np.linspace(0, x_brach[-1], 300)
y_line = np.linspace(0, y_brach[-1], 300)

# === Kugelbewegung entlang der beiden Bahnen ===
frames = 100
t_vals = np.linspace(0, np.pi, frames)
x_b = r * (t_vals - np.sin(t_vals))
y_b = r * (1 - np.cos(t_vals))  # positiv

x_l = np.linspace(0, x_b[-1], frames)
y_l = np.linspace(0, y_b[-1], frames)

# === Ploterstellung ===
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_brach, y_brach, label="Zykloide (Brachistochrone)", linewidth=2)
ax.plot(x_line, y_line, '--', label="Gerade Bahn", linewidth=2)

ball_b, = ax.plot([], [], 'o', color='blue', markersize=10, label="Kugel (Zykloide)")
ball_l, = ax.plot([], [], 'o', color='red', markersize=10, label="Kugel (Gerade)")

ax.set_xlim(0, x_brach[-1])
ax.set_ylim(0, y_brach[-1] + 0.1)  # 0 oben, größere Werte unten
ax.invert_yaxis()  # Wichtig für richtige Darstellung!
ax.set_title("Murmelrennen: Wer ist schneller?")
ax.set_xlabel("Horizontaler Abstand")
ax.set_ylabel("Höhe")
ax.axis("equal")
ax.grid(True)
ax.legend()

# === Animationsfunktion ===
def update(frame):
    ball_b.set_data([x_b[frame]], [y_b[frame]])
    ball_l.set_data([x_l[frame]], [y_l[frame]])
    return ball_b, ball_l

ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# === Ausgabe als GIF (funktioniert ohne ffmpeg) ===
ani.save("brachistochrone_animation.gif", writer="pillow", fps=20)
print("✅ Animation gespeichert als 'brachistochrone_animation.gif'")

# === Video speichern (optional) ===
ani.save("brachistochrone_animation.mp4", writer="ffmpeg", fps=30)
print("✅ Animation gespeichert als 'brachistochrone_animation.mp4'")