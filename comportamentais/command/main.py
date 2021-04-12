from third_party_libraries.light import Light
from third_party_libraries.stereo import Stereo
from commands.light_on_command import LightOnCommand
from commands.light_off_command import LightOffCommand
from commands.stereo_on_with_cd_command import StereoOnWithCdCommand
from remote_control import RemoteControl


class Application():
    def __init__(self, remote_control: RemoteControl):
        self._remote_control = remote_control

    def use_remote_control_on(self, slot):
        self._remote_control.on_button_was_pushed(slot)
    
    def use_remote_control_off(self, slot):
        self._remote_control.off_button_was_pushed(slot)


def create_remote_control():
    remote_control = RemoteControl()

    living_room_light = Light("Living Room")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    stereo_on_with_cd = StereoOnWithCdCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, stereo_on_with_cd, None)

    return remote_control

def main():
    app = Application(create_remote_control())
    app.use_remote_control_on(0)
    app.use_remote_control_on(1)

if __name__ == "__main__":
    main()
