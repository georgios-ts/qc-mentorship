from .pauli_rotation import PauliRotationCommutation



class XRZCommutation(PauliRotationCommutation):
    """
    If back is set to True,
    apply the following identity to enable other optimizations.
            input:
                     ┌───────┐┌────────┐
                q_0: ┤ RZ(φ) ├┤ RX(pi) ├
                     └───────┘└────────┘
            output:
                     ┌────────┐┌────────┐
                q_0: ┤ RX(pi) ├┤ RZ(-φ) ├
                     └────────┘└────────┘

    If it is set to False,
    the reverse transformation is applied.
    """

    def __init__(self, back):
        super().__init__(pauli='x', rotation='rz', back=back)
