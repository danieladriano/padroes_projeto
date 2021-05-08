from facebook_notifier import FacebookNotifier
from sms_notifier import SmsNotifier
from slack_notifier import SlackNotifier
from notifier import Notifier


class Application():
    def __init__(self, notifier):
        self._notifier = notifier

    def send_messages(self):
        self._notifier.send("Sistemas de informação - Estácio")


if __name__ == "__main__":
    email = Notifier()
    facebook = FacebookNotifier(email)
    sms = SmsNotifier(facebook)
    slack  = SlackNotifier(sms)

    app = Application(slack)
    app.send_messages()
