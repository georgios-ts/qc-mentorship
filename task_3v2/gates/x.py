import numpy as np
from .gate import Gate


class X(Gate):
    """ Pauli X gate """
    def __init__(self, qubits):
        super().__init__(name='X', qubits=qubits)

    @property
    def matrix(self):
        return np.array([[0, 1],
                         [1, 0]])

    def unroll(self):
        from .rx import Rx
        
        rules = [Rx(np.pi, self.qubits)]
        phase = np.pi / 2

        return rules, phase
