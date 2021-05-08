from notifier_decorator import NotifierDecorator


class SmsNotifier(NotifierDecorator):
    def send(self, message: str):
        self._notifier.send(message)
        print(f"Send SMS message - {message}")
