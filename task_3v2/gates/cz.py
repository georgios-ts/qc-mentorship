import numpy as np
from .gate import Gate


class CZ(Gate):
    """ Controlled Z - gate """
    def __init__(self, qubits):
        super().__init__(name='CZ', qubits=qubits)

    @property
    def matrix(self):
        return np.array([[1, 0, 0,  0],
                         [0, 1, 0,  0],
                         [0, 0, 1,  0],
                         [0, 0, 0, -1]])

    def unroll(self):
        return [self], 0.0
