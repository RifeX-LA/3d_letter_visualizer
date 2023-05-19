import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


def add_cube(x: int, y: int, z: int, ax):
    vertices = np.array([[x, y, z],
                         [x + 1, y, z],
                         [x + 1, y + 1, z],
                         [x, y + 1, z],
                         [x, y, z + 1],
                         [x + 1, y, z + 1],
                         [x + 1, y + 1, z + 1],
                         [x, y + 1, z + 1]])

    # Define the faces of the cube
    faces = np.array([[0, 1, 2, 3],  # bottom
                      [4, 5, 6, 7],  # top
                      [0, 1, 5, 4],  # front
                      [2, 3, 7, 6],  # back
                      [1, 2, 6, 5],  # right
                      [0, 3, 7, 4]])  # left

    colors = np.array([(0, 0, 1, 1)] * len(faces))

    # Plot the cube
    for i in range(len(faces)):
        x = vertices[faces[i], 0]
        y = vertices[faces[i], 1]
        z = vertices[faces[i], 2]
        ax.add_collection3d(
            mplot3d.art3d.Poly3DCollection([list(zip(x, y, z))], facecolor=colors[i]))


def add_letter(ax, y: int = 0):
    for z in range(0, 6):
        add_cube(0, y, z, ax)

    for x in range(1, 4):
        add_cube(x, y, 5, ax)

    for x in range(1, 4):
        add_cube(x, y, 0, ax)

    for x in range(1, 4):
        add_cube(x, y, 2, ax)

    add_cube(3, y, 1, ax)


def draw_letter():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    add_letter(ax)
    add_letter(ax, 1)

    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)

    plt.show()
