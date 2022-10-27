# Email Discord Bot

A discord bot that forwards every received email in your inbox to a discord using webhooks.
Filters can be used to only select certain mails.

## Usage
Create the `config.py` file based on the file `config.template.py`. The field `IMAP_TOOL_FILTER` is a filter based on the imap_tool library (see [Search Criteria section](https://github.com/ikvk/imap_tools#search-criteria)).
An example of `IMAP_TOOL_FILTER` could be:
```python
IMAP_TOOL_FILTER = AND(
    NOT(subject='re:'), #exclude answers
    NOT(to='someone@example.com'), # exclude an email
    from_="someoneelse@example.com" #anly get emails from this person
)
```

Install impa_tool library:
```bash
pip3 install imap_tool
```

Then run simply:
```bash
python3 main.py`
```