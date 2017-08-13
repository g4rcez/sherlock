from re import sub
from socket import gethostbyname
from utils.UrlUtils import UrlUtils
from webpkg.WebRequest import WebRequest


class Server:
    def __init__(self, url):
        self._allips = []
        self.__setIp(url)
        self.__setJson(self.getIp())

    def __setIp(self, url):
        try:
            if UrlUtils.containsHTTP:
                url = url.replace('http://','')
                url = url.replace('https://','')
                url = sub('/.*','',url)
                self.__listOfIps(gethostbyname(url))
            else:
                self.__listOfIps(gethostbyname(url))
        except:
            pass

    def getIp(self):
        try:
            return self._allips[-1]
        except:
            return ''

    def getJson(self):
        return self._json

    def __setJson(self, ip):
        self._json = WebRequest.getJsonFromLink('http://freegeoip.net/json/' + ip)

    def getLatitude(self):
        return self.getJson()['latitude']

    def getlongitude(self):
        return self.getJson()['longitude']

    def getGeoLocation(self):
        try:
            return "http://maps.google.com/?q=" + str(self.getLatitude()) + ',' + str(self.getlongitude())
        except:
            return ''

    def __listOfIps(self, string):
        self._allips.append(string)
