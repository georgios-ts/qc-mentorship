class Circuit:
    """ A class representing a Quantum Circuit as a list of Gate objects. """
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.gates = []

    def append(self, gate):
        self.gates.append(gate)

    def __str__(self):
        return '\n'.join(str(gate) for gate in self.gates)
