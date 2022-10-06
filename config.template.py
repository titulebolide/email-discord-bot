from imap_tools import AND, NOT
MAIL_HOST = "gmail.imap.com"
MAIL_USER = "user@mail.com"
MAIL_PASSWORD = "asuperbpassword"
MAIL_FOLDER = "mail-folder"
REFRESH_DELAY_SEC = 10*60
DISCORD_WEBHOOK = "discord-webhook"
IMAP_TOOLS_FILTER = AND(
    NOT(subject='re:'), 
    NOT(from_='webmaster@chvd.org'),
    to="chvd@groups.io"
)