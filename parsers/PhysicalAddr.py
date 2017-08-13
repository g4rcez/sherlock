from re import findall
from webpkg.WebRequest import WebRequest
from utils.StringManipulate import StringManipulate


class Physical:
    def __init__(self):
        self._json = None
        self._ceps = []
        self._cep = ''
        self._address = []

    def getHTML(self):
        return self._html

    def setHTML(self, html):
        self._html = html

    def setJson(self, json):
        self._json = json

    def getJson(self):
        return self._json

    def getCep(self):
        try:
            return self._ceps[-1]
        except:
            return None

    def _allCeps(self, string):
        self._ceps.append(string)

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
        try:
            return '[' + self.getCep() + '] ' + self.getLogradouro() + ' (' + self.getComplemento() + '), ' + self.getBairro() + '. ' + self.getCidade() + ', ' + self.getEstado()
        except:
            return ''

    def setFullAddress(self):
        try:
            tmp = '[' + self.getCep() + '] ' + self.getLogradouro() + ' (' + self.getComplemento() + '), ' + self.getBairro() + '. ' + self.getCidade() + ', ' + self.getEstado()
            if tmp not in self._address:
                self._address.append(tmp)
        except:
            pass
