from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import Gate

class EvenBlock(Gate):

    def __init__(self, num_qubits, theta, label=None):
        super().__init__('even block', num_qubits,
                         theta, label)

    def _define(self):
        nqubits = self.num_qubits

        q  = QuantumRegister(nqubits, 'q')
        qc = QuantumCircuit(q,
                            name=self.name)

        for i in range(nqubits):
            qc.rz(self.params[i], i)

        for i in range(nqubits):
            for j in range(i + 1, nqubits):
                qc.cz(i, j)

        self.definition = qc


class OddBlock(Gate):

    def __init__(self, num_qubits, theta, label=None):
        super().__init__('odd block', num_qubits,
                         theta, label)

    def _define(self):
        nqubits = self.num_qubits

        q  = QuantumRegister(nqubits, 'q')
        qc = QuantumCircuit(q,
                            name=self.name)

        for i in range(nqubits):
            qc.rx(self.params[i], i)

        self.definition = qc
