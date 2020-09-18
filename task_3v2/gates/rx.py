import numpy as np
from .gate import Gate


class Rx(Gate):
    """ Rotation around X - axis """
    def __init__(self, angle, qubits):
        super().__init__(name='Rx',
                         qubits=qubits,
                         angle=angle)

    @property
    def matrix(self):
        angle = float(self.angle)
        return np.array([[np.cos(angle / 2), -1j * np.sin(angle / 2)],
                         [-1j * np.sin(angle / 2),  np.cos(angle / 2)]])

    def unroll(self):
        return [self], 0.0
