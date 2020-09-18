import numpy as np
from .gate import Gate


class CX(Gate):
    """ Controlled NOT - gate """
    def __init__(self, qubits):
        super().__init__(name='CX', qubits=qubits)

    @property
    def matrix(self):
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 0, 1],
                         [0, 0, 1, 0]])

    def unroll(self):
        from .rz import Rz
        from .rx import Rx
        from .cz import CZ

        # CX = H CZ H_dag
        rules = [Rz(np.pi / 2, self.qubits[1]),
                 Rx(np.pi / 2, self.qubits[1]),
                 CZ(self.qubits),
                 Rx(-np.pi / 2, self.qubits[1]),
                 Rz(-np.pi / 2, self.qubits[1]),]

        return rules, 0.0
