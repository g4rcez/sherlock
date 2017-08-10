from re import findall
from webpkg.WebRequest import WebRequest
from utils.StringManipulate import StringManipulate


class Physical:
    def __init__(self, html):
        self.html = html
        self.json = ''
        self.cep = ''

    def getCep(self):
        cepList = findall(r'[0-9]{5}-[0-9]{3}', self.html)
        ceps = []
        if len(cepList) > 1:
            cepList.sort()
            for cep in cepList:
                if cep not in ceps:
                    ceps.append(cep)
            for maybecep in ceps:
                cep = StringManipulate.removeNonNumbers(maybecep)
                self.json = WebRequest.getJsonFromLink('http://api.postmon.com.br/v1/cep/' + cep)
                if self.json is None:
                    self.cep = cep
                    return cep
        return None

    def getBairro(self):
        return self.json['bairro']

    def getCidade(self):
        return self.json['cidade']

    def getLogradouro(self):
        return self.json['logradouro']

    def getEstadoSigla(self):
        return self.json['estado']

    def getEstado(self):
        return self.json['estado_info']['nome']

    def getComplemento(self):
        return self.json['complemento']

    def getAddress(self):
        return '[' + self.cep + ']' + self.getLogradouro() + '(' + self.getComplemento() + '), ' + self.getBairro() + '. ' + self.getCidade() + ', ' + self.getEstado()
