from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import BasisTranslator, DAGFixedPoint

from library import BasisLibrary
from optimization import (
    Optimize1qRotations,
    CZRZCommutation, XRZCommutation, ZRXCommutation
)



class RxzCzTrasnpiler:
    """ A class to wrap circuit decomposition into  Rx, Rz, CZ basis. """

    def __init__(self, optimize=False):
        self.optimize = optimize

    def run(self, qc):
        pass_ = BasisTranslator(BasisLibrary,
                                ['rx', 'rz', 'cz'])

        pm = PassManager(pass_)

        if self.optimize:
            def _opt_control(property_set):
                return not property_set['dag_fixed_point']

            pass_ = [Optimize1qRotations('rx'), Optimize1qRotations('rz'),
                     XRZCommutation(back=True), ZRXCommutation(back=False), CZRZCommutation(back=True),
                     DAGFixedPoint()]

            # run until we reach a fixed point and no further changes can be made.
            pm.append(pass_, do_while=_opt_control)


        circ = pm.run(qc)

        return circ
