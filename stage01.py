import arcade
import numpy as np

class Stage1():
    def __init__(self):
        pass

    def rotation(delta_line):
        """
        2D Rotational matrix is given as such:
        [
            (cos(theta), -sin(theta))
            (sin(theta), cos(theta))
        ]

        Counterclockwise rotation is:
        [
            (cos(theta), sin(theta)),
            (-sin(theta), cos(theta))
        ]
        """
        B = np.matrix(([], []))