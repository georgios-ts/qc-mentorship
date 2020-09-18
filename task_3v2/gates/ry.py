import numpy as np
from .gate import Gate


class Ry(Gate):
    """ Rotation around Y - axis """
    def __init__(self, angle, qubits):
        super().__init__(name='Ry',
                         qubits=qubits,
                         angle=angle)

    @property
    def matrix(self):
        angle = float(self.angle)
        return np.array([[np.cos(angle / 2), -np.sin(angle / 2)],
                         [np.sin(angle / 2),  np.cos(angle / 2)]])

    def unroll(self):
        from .rx import Rx
        from .rz import Rz

        rules = [Rz(np.pi / 2, self.qubits),
                 Rx(self.angle, self.qubits),
                 Rz(np.pi / 2, self.qubits)]
                 
        phase = np.pi / 2

        return rules, phase
