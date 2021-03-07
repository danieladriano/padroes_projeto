class House():
    def __init__(self):
        self._parts = []

    def add(self, part):
        self._parts.append(part)

    def list_parts(self):
        print(f"House parts: {', '.join(self._parts)}")
