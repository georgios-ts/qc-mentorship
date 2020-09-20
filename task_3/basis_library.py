from qiskit.converters import circuit_to_dag

class BasisLibrary():
    """ Mapping of gates to equivalent definitions. """

    def __init__(self):
        self._map = {}


    def add(self, gate, _def):
        self._map[gate] = (circuit_to_dag(_def), _def.parameters)


    def __getitem__(self, gate):
        return self._map[gate]


    def __iter__(self):
        return iter(self._map)
