from devices.device_interface import DeviceInterface


class BasicRemote():
    _device: DeviceInterface

    def __init__(self, device: DeviceInterface):
        self._device = device

    def toggle_power(self):
        if self._device.is_enable():
            self._device.disable()
        else:
            self._device.enable()

    def volume_up(self):
        if self._device.is_enable():
            if self._device.get_volume() < 10:
                self._device.set_volume(self._device.get_volume() + 1)
                print(f"Volume {self._device.get_volume()}")

    def volume_down(self):
        if self._device.is_enable():
            if self._device.get_volume() > 0:
                self._device.set_volume(self._device.get_volume() - 1)
                print(f"Volume {self._device.get_volume()}")

    def channel_up(self):
        if self._device.is_enable():
            self._device.set_channel(self._device.get_channel() + 1)
            print(f"Channel {self._device.get_channel()}")

    def channel_down(self):
        if self._device.is_enable():
            self._device.set_channel(self._device.get_channel() - 1)
            print(f"Channel {self._device.get_channel()}")
