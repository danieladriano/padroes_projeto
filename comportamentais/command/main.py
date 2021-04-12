from third_party_libraries.light import Light
from third_party_libraries.stereo import Stereo
from commands.light_on_command import LightOnCommand
from commands.light_off_command import LightOffCommand
from commands.stereo_on_with_cd_command import StereoOnWithCdCommand
from remote_control import RemoteControl


def main():
    remote_control = RemoteControl()

    living_room_light = Light("Living Room")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    stereo_on_with_cd = StereoOnWithCdCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, stereo_on_with_cd, None)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)

    remote_control.on_button_was_pushed(1)

if __name__ == "__main__":
    main()
