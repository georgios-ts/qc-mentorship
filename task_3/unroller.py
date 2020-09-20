from itertools import zip_longest

from qiskit.converters import dag_to_circuit, circuit_to_dag
from qiskit.transpiler.basepasses import TransformationPass



class Unroller(TransformationPass):
    """ A pass to decomposite a circuit into a basis
          using the equivalent circuits defined in library. """

    def __init__(self, library, basis):
        super().__init__()
        self.libr = library
        self.basis = basis


    def run(self, dag):

        for node in dag.op_nodes():

            # if not a basis gate, decompose.
            if node.name not in self.basis:
                if node.name not in self.libr:
                    raise KeyError('No rule to unroll {} gate'.format(node.name))

                equiv_dag, equiv_params = self.libr[node.name]

                if node.op.params:
                    # to circuit in order to bind parameters.
                    equiv_qc = dag_to_circuit(equiv_dag)
                    equiv_qc.assign_parameters(
                                    dict(zip_longest(equiv_params, node.op.params)),
                                    inplace=True)

                    equiv_dag  = circuit_to_dag(equiv_qc)

                dag.substitute_node_with_dag(node,
                                             equiv_dag)
                dag.global_phase += equiv_dag.global_phase

        return dag
