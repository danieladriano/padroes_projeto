class Engine():
    def __init__(self, engine_type):
        self._engine_type = engine_type

    def set_engine_type(self, engine_type):
        self._engine_type = engine_type

    def get_engine_type(self):
        return self._engine_type
