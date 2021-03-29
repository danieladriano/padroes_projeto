from notifier_decorator import NotifierDecorator


class SlackNotifier(NotifierDecorator):
    def send(self, message: str):
        self._notifier.send(message)
        print(f"Send Slack message - {message}")
