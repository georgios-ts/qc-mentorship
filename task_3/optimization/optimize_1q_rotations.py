from itertools import groupby
from numpy import pi, sign

from qiskit.transpiler.basepasses import TransformationPass
from qiskit.circuit.library.standard_gates import RXGate, RZGate



# Similar to Optimize1qGates  of Qiskit
class Optimize1qRotations(TransformationPass):
    """ Optimize chains of single-qubit Rx or Rz gates by combining them into a single gate. """

    def __init__(self, gate, eps=1e-15):

        if gate not in ['rx', 'rz']:
            raise NotImplementedError('Currently only \'rx\' and \'rz\' gates are supported.')

        super().__init__()
        self.gate = gate
        self.eps = eps

    def run(self, dag):

        runs = dag.collect_runs([self.gate])
        runs = _split_runs_on_parameters(runs)

        for group in runs:
            angle = sum([float(node.op.params[0]) for node in group])
            angle = sign(angle) * (abs(angle) % (2 * pi))

            # for angles multiple of 2*pi (numerically close),
            #  the gates act as an identity (up to a global phase).
            if abs(angle) < self.eps:
                dag.remove_op_node(group[0])
            else:
                if self.gate == 'rx':
                    new_op = RXGate(angle)
                elif self.gate == 'rz':
                    new_op = RZGate(angle)

                dag.substitute_node(group[0], new_op,
                                    inplace=True)
            for node in group[1:]:
                dag.remove_op_node(node)

        return dag


def _split_runs_on_parameters(runs):
    """Finds runs containing parameterized gates and splits them into sequential
    runs excluding the parameterized gates.
    """

    out = []
    for run in runs:
        groups = groupby(run, lambda x: x.op.is_parameterized())

        for group_is_parameterized, gates in groups:
            if not group_is_parameterized:
                out.append(list(gates))

    return out
