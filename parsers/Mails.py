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
            self._emails.append(email)
        list(set(self._emails))

    def setEmails(self, html):
        self.setHTML(html)
        emails = findall('[A-Za-z+_.]+@[A-Za-z]+\..*', self.getHTML())
        maillist = []
        if len(emails) > 0:
            for links in emails:
                email = sub(r'".*', '', str(links))
                email = sub(r"'.*", '', email).strip()
                maillist.append(email)
            self.__setEmailsForList(maillist)

    def getEmails(self):
        return self._emails
