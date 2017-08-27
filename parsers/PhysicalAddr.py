from re import findall
from parsers.Parser import Parser
from webpkg.WebRequest import WebRequest
from utils.StringManipulate import StringManipulate


class Physical(Parser):
    def __init__(self, html = '', arrayList = []):
        Parser.__init__(self, html, arrayList)
        self._json = None
        self._ceps = []
        self._address = []

    def getHTML(self):
        return self._html

    def setHTML(self, html):
        self._html = html

    def setJson(self, json):
        self._json = json

    def getJson(self):
        return self._json

    def getLastCep(self):
        try:
            return self._ceps[-1]
        except:
            return None

    def getAllCeps(self):
        try:
            return self._ceps
        except:
            return None

    def _allCeps(self, string):
        self._ceps.append(string)

    def getCepFromWeb(self, givenCep):
        for givenCep in self.getAllCeps():
            self.setJson(WebRequest.getJsonFromLink('http://api.postmon.com.br/v1/cep/' + givenCep))
            if self.getJson() is not None:
                return givenCep

    def setCep(self, html):
        self.setHTML(html)
        cepList = findall(r'[0-9]{5}-[0-9]{3}', self.getHTML())
        ceps = []
        if len(cepList) > 0:
            cepList.sort()
            for cep in cepList:
                if cep not in ceps:
                    ceps.append(cep)
            for maybecep in ceps:
                cep = StringManipulate.removeNonNumbers(maybecep)
                if WebRequest.isActiveLink('http://api.postmon.com.br/v1/cep/' + cep) and cep not in self.getAllCeps():
                    self._allCeps(cep)

    def getBairro(self):
        return self.getJson()['bairro']

    def getCidade(self):
        return self.getJson()['cidade']

    def getLogradouro(self):
        return self.getJson()['logradouro']

    def getEstadoSigla(self):
        return self.getJson()['estado']

    def getEstado(self):
        return self.getJson()['estado_info']['nome']

    def getComplemento(self):
        return self.getJson()['complemento']

    def getAddress(self, cep):
        try:
            return '[' + self.getCepFromWeb(cep) + '] ' + self.getLogradouro() + ' (' + self.getComplemento() + '), ' + self.getBairro() + '. ' + self.getCidade() + ', ' + self.getEstado()
        except:
            return ''

    def setFullAddress(self, cep):
        try:
            tmp = '[' + self.getCepFromWeb(cep) + '] ' + self.getLogradouro() + ' (' + self.getComplemento() + '), ' + self.getBairro() + '. ' + self.getCidade() + ', ' + self.getEstado()
            if tmp not in self._address:
                self._address.append(tmp)
        except:
            pass
