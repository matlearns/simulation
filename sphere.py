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
# We define the X, Y, and Z coordinates for the start and end of the line
# Start point: (0, 0, 0) -> The center
# End point:   (0, 0, 1) -> The top/North Pole
x_line = [0, 0]
y_line = [0, 0]
z_line = [0, 1]


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
        xaxis=dict(title='X Axis', range=[-1.5, 1.5]),
        yaxis=dict(title='Y Axis', range=[-1.5, 1.5]),
        zaxis=dict(title='Z Axis', range=[-1.5, 1.5]),
        aspectratio=dict(x=1, y=1, z=1)
    )
)

fig.show()