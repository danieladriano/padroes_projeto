class Stereo():
    def __init__(self, desc: str):
        self._desc = desc

    def on(self):
        print(f"{self._desc} Stereo is on!!")

    def off(self):
        print(f"{self._desc} Stereo is off!!")

    def set_cd(self):
        print(f"{self._desc} Stereo set CD!!")

    def set_dvd(self):
        print(f"{self._desc} Stereo set DVD!!")

    def set_radio(self):
        print(f"{self._desc} Stereo set Radio!!")

    def set_volume(self, vol: int):
        print(f"{self._desc} Stereo volume set to {vol}!!")
