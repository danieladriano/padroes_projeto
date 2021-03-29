from notifier_interface import NotifierInterface


class NotifierDecorator(NotifierInterface):
    _notifier: NotifierInterface = None
    def __init__(self, notifier: NotifierInterface):
        self._notifier = notifier

    @property
    def notifier(self) -> str:
        return self._notifier

    def send(self, message: str):
        self._notifier.send()
