import numpy as np
import matplotlib.pyplot as plt

def main():
    v1 = [0,1]
    v2 = [1,0]
    #matrix given as partials [[du/dx, du/dy], [dv/dx, dv/dy]]
    transformation_matrix = [[2,0.2],[0.0,2]]
    plot_jacobian_trans(v1,v2, transformation_matrix)

def plot_jacobian_trans(v1_xy, v2_xy, transformation_matrix):
    # vectors on plane 1 (x,y)
    v1_xy = np.array(v1_xy)
    v2_xy = np.array(v2_xy)
    v3_xy = v1_xy + v2_xy
    area_xy = abs(v1_xy[0]*v2_xy[1] - v1_xy[1]*v2_xy[0])

    # vectors on plane 2 (u, v)
    v1_uv = transformation_matrix @ v1_xy
    v2_uv = transformation_matrix @ v2_xy
    v3_uv = v1_uv + v2_uv
    
    # Calculate jacobian term
    jacobian = np.linalg.det(transformation_matrix)
    area_uv = abs(v1_uv[0]*v2_uv[1] - v1_uv[1]*v2_uv[0])

    # Create figure with both plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Parallelogram on Plane 1 (x, y)
    ax1.fill([0, v1_xy[0], v3_xy[0], v2_xy[0]], [0, v1_xy[1], v3_xy[1], v2_xy[1]], 
             facecolor='blue', alpha=0.2)
    ax1.quiver([0, 0], [0, 0], [v1_xy[0], v2_xy[0]], [v1_xy[1], v2_xy[1]], 
               color=['blue', 'red'], angles='xy', scale_units='xy', scale=1)
    ax1.set_title(f"Plane (x,y)\nArea = {area_xy}")

    # Parallelogram on Plane 2 (u, v)
    ax2.fill([0, v1_uv[0], v3_uv[0], v2_uv[0]], [0, v1_uv[1], v3_uv[1], v2_uv[1]], 
             facecolor='green', alpha=0.2)
    ax2.quiver([0, 0], [0, 0], [v1_uv[0], v2_uv[0]], [v1_uv[1], v2_uv[1]], 
               color=['blue', 'red'], angles='xy', scale_units='xy', scale=1)
    ax2.set_title(f"Plane (u,v)\nJacobian |det(A)| = {abs(jacobian):.2f}\nNew Area = {area_uv:.2f}")

    # adjust graphs in figure
    for ax in [ax1, ax2]:
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.grid(True, linestyle='--')
        ax.set_aspect('equal')
        ax.set_xlim(-1, max(v3_xy[0], v3_uv[0], 2) + 1)
        ax.set_ylim(-1, max(v3_xy[1], v3_uv[1], 2) + 1)

    plt.tight_layout()
    plt.show()
if __name__=="__main__":
    main()