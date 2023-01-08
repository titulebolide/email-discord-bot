# Email To Discord Bot

A discord bot that forwards every received email in your inbox to a discord using webhooks.
Filters can be used to only select certain mails.

## Usage
Create the `email-to-discord.conf` file based on the file `config.template.py`. The field `filter` is a filter based on the imap_tool library (see [Search Criteria section](https://github.com/ikvk/imap_tools#search-criteria)).
An example of `filter` could be:
```
filter = AND(NOT(subject='re:'), # exclude answers
    NOT(to='someone@example.com'), # exclude an email
    from_="someoneelse@example.com" # only get emails from this person
    )
```

Install the requirements:
```bash
pip3 install -r requirements.txt
```

Then run simply:
```bash
python3 -m email-to-discord`
```