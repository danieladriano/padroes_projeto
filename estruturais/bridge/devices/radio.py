from devices.device_interface import DeviceInterface


class Radio(DeviceInterface):
    _enable = False
    _volume = 0
    _channel = 0

    def is_enable(self) -> bool:
        return self._enable

    def enable(self):
        self._enable = True

    def disable(self):
        self._enable = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int):
        self._volume = volume

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int):
        self._channel = channel
