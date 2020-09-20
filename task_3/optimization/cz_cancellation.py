from qiskit.transpiler.basepasses import TransformationPass



class CZCancellation(TransformationPass):
    """ Remove even number of consecutive CZ gates. """

    def __init__(self):
        super().__init__()


    def run(self, dag):

        for run in dag.collect_runs('cz'):
            keep = len(run) % 2    # if odd keep one, else remove them all.
            for node in run[keep:]:
                dag.remove_op_node(node)

        return dag
