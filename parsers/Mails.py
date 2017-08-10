from re import sub
from re import findall


class Mail:
    def __init__(self, html):
        self.html = html

    def getMails(self):
        emails = findall('[A-Za-z+_.]+@[A-Za-z]+\..*', self.html)
        maillist = []
        if len(emails) > 0:
            for links in emails:
                if links not in maillist:
                    email = sub(r'".*', '', str(links))
                    email = sub(r"'.*", '', email).strip()
                    maillist.append(email)
            maillist.sort()
            return maillist
        return None
