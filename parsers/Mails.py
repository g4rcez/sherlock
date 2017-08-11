from re import sub
from re import findall


class Mail:
    def __init__(self):
        self._emails = []

    def getHTML(self):
        return self._html

    def setHTML(self, html):
        self._html = html

    def __setEmailsForList(self, arrayList):
        for email in arrayList:
            if email not in self._emails:
                self._emails.append(email)
        self._emails.sort()

    def setEmails(self, html):
        self.setHTML(html)
        emails = findall('[A-Za-z+_.]+@[A-Za-z]+\..*', self.getHTML())
        maillist = []
        if len(emails) > 0:
            for links in emails:
                if links not in maillist:
                    email = sub(r'".*', '', str(links))
                    email = sub(r"'.*", '', email).strip()
                    maillist.append(email)
            self.__setEmailsForList(maillist)

    def getEmails(self):
        return self._emails
