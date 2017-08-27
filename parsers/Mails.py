from re import sub
from re import findall
from parsers.Parser import Parser
from utils.StringManipulate import StringManipulate

class Mail(Parser):
    def __init__(self, html = '', lista = []):
        Parser.__init__(self, html, lista)
        self._emails = []

    def setEmails(self, html):
        self.setHTML(html)
        emails = findall('[A-Za-z+_.]+@[A-Za-z]+\..*', self.getHTML())
        maillist = []
        if len(emails) > 0:
            for links in emails:
                email = sub(r'".*', '', str(links))
                email = sub(r"'.*", '', email).strip()
                email = StringManipulate.removeSpecifieds(email, [
                    '<br>','<','>','\\','/','?','(',')','{','}','"',"'",',',';'
                ])
                maillist.append(email.split(' ')[0])
            self._emails = self.organizeList(maillist)

    def getEmails(self):
        return self._emails
