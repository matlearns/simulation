import numpy as np
import plotly.graph_objects as go

# --- 1. THE SPHERE CODE ---
r = 1.3
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

x_sphere = r * np.sin(phi) * np.cos(theta)
y_sphere = r * np.sin(phi) * np.sin(theta)
z_sphere = r * np.cos(phi)

# --- 2. THE STRAIGHT LINE DATA ---
print("Enter line start and end coordinates:")
x_start = float(input("  X start: "))
x_end   = float(input("  X end:   "))
y_start = float(input("  Y start: "))
y_end   = float(input("  Y end:   "))
z_start = float(input("  Z start: "))
z_end   = float(input("  Z end:   "))

x_line = [x_start, x_end]
y_line = [y_start, y_end]
z_line = [z_start, z_end]

print("\nEnter axis ranges:")
x_min = float(input("  X axis min: "))
x_max = float(input("  X axis max: "))
y_min = float(input("  Y axis min: "))
y_max = float(input("  Y axis max: "))
z_min = float(input("  Z axis min: "))
z_max = float(input("  Z axis max: "))


# --- 3. PLOTTING BOTH TOGETHER ---
fig = go.Figure()

# Add the sphere surface
fig.add_trace(go.Surface(
    x=x_sphere, y=y_sphere, z=z_sphere,
    colorscale='Viridis',
    opacity=0.6, # Making the sphere slightly see-through so we can see the line inside!
    showscale=False # Hides the color bar to keep it clean
))

# Add the straight line
fig.add_trace(go.Scatter3d(
    x=x_line, y=y_line, z=z_line,
    mode='lines+markers', # Draws a line with dots at the endpoints
    line=dict(color='red', width=20), # Makes the line thick and red
    marker=dict(size=4, color='blue') # Puts black dots at the center and pole
))

# --- 4. LAYOUT ---
fig.update_layout(
    title="Line Inside a 3D Sphere",
    scene=dict(
        xaxis=dict(title='X Axis', range=[x_min, x_max]),
        yaxis=dict(title='Y Axis', range=[y_min, y_max]),
        zaxis=dict(title='Z Axis', range=[z_min, z_max]),
        aspectratio=dict(x=1, y=1, z=1)
    )
)

fig.show()