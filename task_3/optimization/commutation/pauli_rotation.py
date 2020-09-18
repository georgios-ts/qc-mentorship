from qiskit.transpiler.basepasses import TransformationPass



class PauliRotationCommutation(TransformationPass):

    def __init__(self, pauli, rotation, back):

        if (pauli, rotation) not in [('x', 'rz'), ('z', 'rx')]:
            raise NotImplementedError

        super().__init__()
        self.back = back
        self.pauli = 'r' + pauli
        self.rotation = rotation

    def run(self, dag):

        pauli_nodes = filter(lambda node: is_pauli(node.op.params[0]),
                            dag.named_nodes(self.pauli))

        for pauli in pauli_nodes:

            if self.back:
                nodes = list(filter(lambda x: x.name == self.rotation,
                                    dag.predecessors(pauli)))
            else:
                nodes = list(filter(lambda x: x.name == self.rotation,
                                    dag.successors(pauli)))

            if nodes:
                assert len(nodes) == 1

                r_node = nodes[0]
                dag.substitute_node(r_node,
                                    pauli.op)

                r_node.op.params[0] = -1 * r_node.op.params[0]
                dag.substitute_node(pauli,
                                    r_node.op)

        return dag


def is_pauli(angle):
    from numpy import pi, allclose

    # angle may be an unbound Parameter.
    try:
        angle = abs(float(angle)) % (2 * pi)
        return allclose(angle, pi)
    except:
        return False
