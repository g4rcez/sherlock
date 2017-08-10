import requests
from json import loads
from re import findall
from urllib.request import urlopen
from utils.StringManipulate import StringManipulate

class Physical():

    def __init__(self, html):
        self.html = html

    def getCep(self):
        cep = findall(r'.*[0-9]{5}-[0-9]{3}.*', self.html)
        cep = ''.join(cep)
        cep = StringManipulate.removeNonNumbers(cep)
        return cep

    def getJson(self):
        try:
            url = 'http://api.postmon.com.br/v1/cep/' + str(self.getCep().replace('-', ''))
            json = urlopen(url)
            return loads(json.read())
        except:
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
        return "[" + self.getCep() + "] " + self.getLogradouro() + " [" + self.getComplemento + '], ' + self.getBairro() + ". " + self.getCidade() + ". " + self.getEstado()
