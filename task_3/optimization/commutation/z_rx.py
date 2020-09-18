from .pauli_rotation import PauliRotationCommutation



class ZRXCommutation(PauliRotationCommutation):
    """
    If back is set to True,
    apply the following identity to enable other optimizations.
            input:
                     ┌───────┐┌────────┐
                q_0: ┤ RX(φ) ├┤ RZ(pi) ├
                     └───────┘└────────┘
            output:
                     ┌────────┐┌────────┐
                q_0: ┤ RZ(pi) ├┤ RX(-φ) ├
                     └────────┘└────────┘

    If it is set to False,
    the reverse transformation is applied.
    """

    def __init__(self, back):
        super().__init__(pauli='z', rotation='rx', back=back)
