from re import sub
from re import findall
from parsers.Parser import Parser
from utils.UrlUtils import UrlUtils


class Lattes(Parser):
    def __init__(self, html = '', arrayList = []):
        Parser.__init__(self, html, arrayList)
        self._lattes = []

    def setLattes(self, html):
        self.setHTML(html)
        all_lattes = findall('http://lattes.cnpq.br/[0-9]{15}', self.getHTML())
        lattes_list = []
        for lattes in all_lattes:
            latte = sub('".*', '', lattes)
            latte = sub(".*'", '', latte).strip()
            lattes_list.append(latte)
        self._lattes = self.organizeList(lattes_list)

    def getLattes(self):
        return self._lattes
