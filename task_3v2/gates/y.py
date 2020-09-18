import numpy as np
from .gate import Gate


class Y(Gate):
    """ Pauli Y gate """
    def __init__(self, qubits):
        super().__init__(name='Y', qubits=qubits)

    @property
    def matrix(self):
        return np.array([[0, -1j],
                         [1j,  0]])

    def unroll(self):
        from .rz import Rz
        from .rx import Rx

        rules = [Rx(np.pi, self.qubits),
                 Rz(np.pi, self.qubits)]
        phase = np.pi / 2

        return rules, phase
