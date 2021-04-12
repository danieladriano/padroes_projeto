from third_party_libraries.light import Light
from commands.command import Command


class LightOffCommand(Command):
    _light: Light

    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.off()
