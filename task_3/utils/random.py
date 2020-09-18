import numpy as np

from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library.standard_gates import (
    HGate,
    ZGate,  XGate,  YGate,
    RZGate, RXGate, RYGate,
    CXGate, CZGate
)


# Similar to random_circuit of Qiskit.
def random_circuit(num_qubits, depth, seed=None):

    if seed is None:
        seed = np.random.randint(0, np.iinfo(np.int32).max)
    rng = np.random.default_rng(seed)

    one_q_ops = [HGate,
                 XGate,  YGate,  ZGate,
                 RXGate, RYGate, RZGate]

    two_q_ops = [CXGate, CZGate]

    one_param = [RXGate, RYGate, RZGate]


    qr = QuantumRegister(num_qubits, 'q')
    qc = QuantumCircuit(qr)

    for _ in range(depth):
        remaining_qubits = list(range(num_qubits))

        while remaining_qubits:
            max_possible_operands = min(len(remaining_qubits), 2)
            num_operands = rng.choice(range(max_possible_operands)) + 1

            rng.shuffle(remaining_qubits)
            operands = remaining_qubits[:num_operands]
            remaining_qubits = [q for q in remaining_qubits if q not in operands]

            if num_operands == 1:
                operation = rng.choice(one_q_ops)
            elif num_operands == 2:
                operation = rng.choice(two_q_ops)

            num_angles = 1 if operation in one_param else 0

            angles = [rng.uniform(- 2*np.pi, 2 * np.pi) for _ in range(num_angles)]
            register_operands = [qr[i] for i in operands]
            op = operation(*angles)

            qc.append(op, register_operands)

    return qc
