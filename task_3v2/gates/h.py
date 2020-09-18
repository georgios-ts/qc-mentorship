import numpy as np
from .gate import Gate


class H(Gate):
    """ Hadamard gate """
    def __init__(self, qubits):
        super().__init__(name='H', qubits=qubits)

    @property
    def matrix(self):
        return (1 / np.sqrt(2)) * np.array([[1,  1],
                                            [1, -1]])

    def unroll(self):
        from .rx import Rx
        from .rz import Rz
        
        rules = [Rz(np.pi / 2, self.qubits),
                 Rx(np.pi / 2, self.qubits),
                 Rz(np.pi / 2, self.qubits)]

        phase = np.pi / 2

        return rules, phase
