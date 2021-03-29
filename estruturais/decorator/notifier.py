from notifier_interface import NotifierInterface


class Notifier(NotifierInterface):
    def send(self, message: str):
        print(f"Send e-mail message - {message}")
