import numpy as np
from .gate import Gate


class Rz(Gate):
    """ Rotation around Z - axis """
    def __init__(self, angle, qubits):
        super().__init__(name='Rz',
                         qubits=qubits,
                         angle=angle)

    @property
    def matrix(self):
        angle = float(self.angle)
        return np.array([[np.exp(-1j * angle / 2), 0],
                         [0,  np.exp(1j * angle / 2)]])

    def unroll(self):
        return [self], 0.0
