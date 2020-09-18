from numpy import pi

from qiskit import QuantumCircuit, QuantumRegister

from qiskit.circuit import Parameter
from qiskit.circuit.equivalence import EquivalenceLibrary

from qiskit.circuit.library.standard_gates import (
    HGate,
    ZGate,  XGate,  YGate,
    RZGate, RXGate, RYGate,
    CXGate, CZGate
)


libr = BasisLibrary = EquivalenceLibrary()


# H - Gate
q = QuantumRegister(1, 'q')
_def = QuantumCircuit(q, global_phase=pi / 2)

rules = [(RZGate(pi / 2), [q[0]], []),
         (RXGate(pi / 2), [q[0]], []),
         (RZGate(pi / 2), [q[0]], [])]

for inst, qargs, cargs in rules:
    _def.append(inst, qargs, cargs)

libr.add_equivalence(HGate(), _def)



# Z - Gate
q = QuantumRegister(1, 'q')
_def = QuantumCircuit(q, global_phase=pi / 2)

rules = [(RZGate(pi), [q[0]], [])]

for inst, qargs, cargs in rules:
    _def.append(inst, qargs, cargs)

libr.add_equivalence(ZGate(), _def)



# X - Gate
q = QuantumRegister(1, 'q')
_def = QuantumCircuit(q, global_phase=pi / 2)

rules = [(RXGate(pi), [q[0]], [])]

for inst, qargs, cargs in rules:
    _def.append(inst, qargs, cargs)

libr.add_equivalence(XGate(), _def)



# Y - Gate
q = QuantumRegister(1, 'q')
_def = QuantumCircuit(q, global_phase=pi / 2)

rules = [(RXGate(pi), [q[0]], []),
         (RZGate(pi), [q[0]], [])]

for inst, qargs, cargs in rules:
    _def.append(inst, qargs, cargs)

libr.add_equivalence(YGate(), _def)



# Ry - Gate
q = QuantumRegister(1, 'q')
_def = QuantumCircuit(q)

theta = Parameter('theta')

rules = [(RZGate(-pi / 2), [q[0]], []),
         (RXGate(theta),  [q[0]], []),
         (RZGate(pi / 2), [q[0]], [])]

for inst, qargs, cargs in rules:
    _def.append(inst, qargs, cargs)

libr.add_equivalence(RYGate(theta), _def)



# CX - Gate
q = QuantumRegister(2, 'q')
_def = QuantumCircuit(q)

rules = [(RZGate(pi / 2), [q[1]], []),
         (RXGate(pi / 2), [q[1]], []),
         (CZGate(), [q[0], q[1]], []),
         (RXGate(-pi / 2), [q[1]], []),
         (RZGate(-pi / 2), [q[1]], [])]

for inst, qargs, cargs in rules:
    _def.append(inst, qargs, cargs)

libr.add_equivalence(CXGate(), _def)
