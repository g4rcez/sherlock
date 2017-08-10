from re import sub
from re import findall


class Lattes:
    def __init__(self, html):
        self.html = html

    def getLattes(self):
        all_lattes = findall('http://lattes.cnpq.br/[0-9]{15}', self.html)
        lattes_list = []
        for lattes in all_lattes:
            latte = sub('".*', '', lattes)
            latte = sub(".*'", '', latte)
            lattes_list.append(latte)
        lattes_list.sort()
        return lattes_list
