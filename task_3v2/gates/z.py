import numpy as np
from .gate import Gate


class Z(Gate):
    """ Pauli Z gate """
    def __init__(self, qubits):
        super().__init__(name='Z', qubits=qubits)

    @property
    def matrix(self):
        return np.array([[1, 0],
                         [0, -1]])

    def unroll(self):
        from .rz import Rz

        rules = [Rz(np.pi, self.qubits)]
        phase = np.pi / 2

        return rules, phase
