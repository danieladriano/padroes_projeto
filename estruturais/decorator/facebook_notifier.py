from notifier_decorator import NotifierDecorator


class FacebookNotifier(NotifierDecorator):
    def send(self, message: str):
        self._notifier.send(message)
        print(f"Send Facebook message - {message}")
