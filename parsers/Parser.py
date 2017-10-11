from collections import OrderedDict


class Parser:
    def __init__(self, html = '', lista = []):
        self.html = html
        self.lista = lista

    def setHTML(self, html):
        self.html = html

    def getHTML(self):
        return self.html

    def organizeList(self, arrayList):
        for item in arrayList:
            self.lista.append(item)
        for newItem in self.lista:
                while self.lista.count(newItem) != 1:
                    self.lista.remove(newItem)
        self.lista = list(OrderedDict.fromkeys(self.lista))
        self.lista = list(set(self.lista))
        return self.lista
