from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import Gate

from blocks import EvenBlock, OddBlock

class Layer(Gate):

    def __init__(self, num_qubits, theta, label=None):
        super().__init__('layer', num_qubits,
                         theta, label)

    def _define(self):
        nqubits = self.num_qubits

        q  = QuantumRegister(nqubits, 'q')
        qc = QuantumCircuit(q,
                            name=self.name)

        theta = self.params[:nqubits] # parameters of odd block
        phi = self.params[nqubits:] # parameters of even block

        rules = [
            (OddBlock(nqubits, theta), q[:], []),
            (EvenBlock(nqubits,  phi), q[:], [])
        ]
        qc._data = rules

        self.definition = qc
