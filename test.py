from imap_tools import AND, NOT, MailBox
import main
import datetime
import config


def get_latest_mails():
    with MailBox(config.MAIL_HOST).login(config.MAIL_USER, config.MAIL_PASSWORD, config.MAIL_FOLDER) as mailbox:
        return list(
            mailbox.fetch(AND(date_gte=(datetime.datetime.now() - datetime.timedelta(days=3)).date()))
        )