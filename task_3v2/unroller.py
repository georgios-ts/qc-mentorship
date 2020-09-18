from numpy import sign, pi
from circuit import Circuit


class Unroller:
    def run(self, qc):
        circ = Circuit(qc.num_qubits)

        global_phase = 0.0

        for gate in qc.gates:
            rules, phase = gate.unroll()
            global_phase += phase

            for basis_gate in rules:
                circ.append(basis_gate)

        global_phase = sign(global_phase) * (abs(global_phase) % (2 * pi))

        return circ, global_phase
