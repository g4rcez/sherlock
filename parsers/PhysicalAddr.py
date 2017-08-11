from re import findall
from webpkg.WebRequest import WebRequest
from utils.StringManipulate import StringManipulate


class Physical:
    def __init__(self, html):
        self._html = html
        self._json = None
        self._ceps = []
        self._cep = self.setCep()

    def getHTML(self):
        return self._html

    def setJson(self, json):
        self._json = json

    def getJson(self):
        return self._json

    def getCep(self):
        return self._ceps[-1]

    def _allCeps(self, string):
        self._ceps.append(string)

    def setCep(self):
        cepList = findall(r'[0-9]{5}-[0-9]{3}', self.getHTML())
        ceps = []
        if len(cepList) > 0:
            cepList.sort()
            for cep in cepList:
                if cep not in ceps:
                    ceps.append(cep)
            for maybecep in ceps:
                cep = StringManipulate.removeNonNumbers(maybecep)
                self.setJson(WebRequest.getJsonFromLink('http://api.postmon.com.br/v1/cep/' + cep))
                if self.getJson() is not None:
                    self._cep = cep
                    self._allCeps(cep)
                    return self.getCep()
        return None

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

    def getAddress(self):
        return '[' + self.getCep() + '] ' + self.getLogradouro() + ' (' + self.getComplemento() + '), ' + self.getBairro() + '. ' + self.getCidade() + ', ' + self.getEstado()