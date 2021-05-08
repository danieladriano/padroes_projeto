from third_party_libraries.stereo import Stereo
from commands.command import Command


class StereoOnWithCdCommand(Command):
    _stereo = Stereo

    def __init__(self, stereo: Stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.set_cd()
        self._stereo.set_volume(10)
