from typing import Union, Optional, List
from abc import ABC, abstractmethod


class Gate(ABC):
    """ A minimal class for representing Quantum Gates. """
    def __init__(self,
                 name: str,
                 qubits: Union[int, List],
                 angle: Optional[int] = None):
        """
            Args:
                  name: Gate name.
                qubits: The qubits the gate act on.
                        For a single qubit gate, this is just an int.
                        For 2q-gates, this is a list.
        """
        self.name = name
        self.qubits = qubits
        self.angle = angle


    @property
    @abstractmethod
    def matrix(self):
        """ Return a Numpy.array for the gate unitary matrix """
        raise NotImplementedError


    @abstractmethod
    def unroll(self):
        """ Decompose the gate into 'RX, RZ, CZ' basis."""
        raise NotImplementedError


    def __str__(self):

        # 1 or 2-qubit gate
        if isinstance(self.qubits, List):
            qubits = ' on q_{} controlled by q_{}'.format(*self.qubits)
        else:
            qubits = ' on q_{}'.format(self.qubits)

        angle = ''
        if self.angle:
            angle = '({0:.3g})'.format(self.angle)

        return self.name + angle + qubits
