from remotes.basic_remote import BasicRemote
from devices.radio import Radio
from devices.tv import Tv


def client(remote):
    print(type(remote._device))
    remote.toggle_power()
    remote.volume_up()
    remote.volume_up()
    remote.volume_up()
    remote.volume_up()

    remote.volume_down()
    remote.volume_down()

if __name__ == "__main__":
    radio = Radio()
    basic_remote = BasicRemote(radio)
    client(basic_remote)

    tv = Tv()
    basic_remote = BasicRemote(tv)
    client(basic_remote)
