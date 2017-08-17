from re import sub
from re import findall
from utils.UrlUtils import UrlUtils


class Lattes:
    def __init__(self):
        self._lattes = []

    def getHTML(self):
        return self._html

    def setHTML(self, html):
        self.__setHTML(html)

    def __setHTML(self, html):
        self._html = html

    def __setLinksForLattes(self, arrayList):
        for link in arrayList:
            self._lattes.append(link)
        list(set(self._lattes))

    def setLattes(self, html):
        self.setHTML(html)
        all_lattes = findall('http://lattes.cnpq.br/[0-9]{15}', self.getHTML())
        lattes_list = []
        for lattes in all_lattes:
            latte = sub('".*', '', lattes)
            latte = sub(".*'", '', latte).strip()
            lattes_list.append(latte)
        self.__setLinksForLattes(lattes_list)

    def getLattes(self):
        return self._lattes
