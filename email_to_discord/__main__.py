import argparse
import logging
import configparser
import os
import socket
import imaplib
import time
import imap_tools
from . import bot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        default="./email-to-discord.conf",
        help="Configuration file path. Default : ./email-to-discord.conf",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Increase verbosity"
    )
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if not os.path.isfile(args.config):
        logging.error("Configuration file not found")
        exit(1)
        
    config = configparser.ConfigParser()
    config.read(args.config)

    mailbox = None
    done = False
    while not done:
        try:
            mailbox = bot.MailBoxHandler(
                config['mail']['host'],
                config['mail']['user'],
                config['mail']['password'],
                config['mail']['folder'],
                config['mail']['filter'],
            )
            mailbox.start_polling()
            while not done:
                logging.info("Refreshing")
                for msg in mailbox.poll():
                    logging.info(f"Sending {msg.subject}")
                    bot.send_mail_to_discord(msg, config['bot']['discord_webhook'])

                time.sleep(config['bot'].getint('refresh_delay'))

        except (
            TimeoutError,
            ConnectionError,
            imaplib.IMAP4.abort,
            imap_tools.MailboxLoginError,
            imap_tools.MailboxLogoutError,
            socket.herror,
            socket.gaierror,
            socket.timeout,
        ) as e:
            if mailbox is not None:
                mailbox.stop_polling()
            logging.error(f"{e} : reconnect in a minute")
            time.sleep(60)

main()
