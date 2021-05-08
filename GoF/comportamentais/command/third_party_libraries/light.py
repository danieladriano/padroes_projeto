class Light():

    def __init__(self, desc: str):
        self._desc = desc

    def on(self):
        print(f"{self._desc} Light is on!!")

    def off(self):
        print(f"{self._desc} Light is off!!")
