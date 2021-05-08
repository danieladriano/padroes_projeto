import copy

class Aircraft():
    """
        Python fornece sua própria interface de Prototype via métodos
        'copy.copy' e  'copy.deepcopy'
    """
    def __init__(self, number_seats, engine):
        self._number_seats = number_seats
        self._engine = engine

    def get_number_seats(self):
        return self._number_seats

    def get_engine(self):
        return self._engine

    def __copy__(self):
        aux_engine = copy.copy(self._engine)
        new = self.__class__(self._number_seats, aux_engine)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo={}):
        aux_engine = copy.deepcopy(self._engine, memo)
        new = self.__class__(self._number_seats, aux_engine)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new
