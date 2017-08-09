import re
import parsers

class email():
    def __init__(self, html):
        self.html = html

    def get_mails(self):
        emails = self.html.findAll('a', attrs={'href': re.compile(".*mailto")})
        maillist = []
        if len(emails) > 0:
            for links in emails:
                email = re.sub('.*mailto:', '', str(links))
                email = re.sub('".*', '', str(email))
                maillist.append(email)
            return maillist
        return None
